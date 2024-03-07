# Assuming this is part of a Flask view or service file

import os
from werkzeug.utils import secure_filename
from flask import current_app, jsonify, request
import speech_recognition as sr
from ..utils import database, helpers

def process_audio_and_transcribe(request):
    if 'audio_file' not in request.files:
        return jsonify({"error": "No audio file part"}), 400
    audio_file = request.files['audio_file']
    if audio_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    reference_text = request.form.get('reference_text', '')
    id_avaliacao = request.form.get('id_avaliacao', '')

    filename = secure_filename(audio_file.filename)
    upload_folder = current_app.config['UPLOAD_FOLDER']

    # Ensure the upload folder exists
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, filename)
    audio_file.save(file_path)

    transcript = helpers.transcribe_audio(file_path)
    if transcript is None:
        os.remove(file_path)
        return jsonify({"error": "Transcription failed"}), 500

    accuracy = helpers.calculate_word_accuracy(transcript, reference_text)
    duration = helpers.get_audio_duration(file_path)
    wpm = helpers.calculate_words_per_minute(transcript, duration)
    word_count = helpers.get_word_count(transcript)
    fluency_level = helpers.determine_reading_level(accuracy)
    
    crdi = helpers.calculate_crdi(transcript, reference_text, duration)

    # Handle the success or failure of data insertion
    if not database.insert_transcription_into_db(transcript, accuracy, word_count, wpm, duration, fluency_level, crdi, id_avaliacao):
        return jsonify({"error": "Failed to insert data into database"}), 500

    os.remove(file_path)

    return jsonify({
        "transcription": transcript,
        "accuracy": accuracy,
        "word_count": word_count,
        "wpm": wpm,
        "duration": duration,
        "fluency_level": fluency_level,
        "crdi": crdi
    }), 200
