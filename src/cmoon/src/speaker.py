#!/usr/bin/env python
# coding: UTF-8 


import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer


def synthesize_to_speaker():
    # Find your key and resource region under the 'Keys and Endpoint' tab in your Speech resource in Azure Portal
    # Remember to delete the brackets <> when pasting your key and region!
    # speech_config = speechsdk.SpeechConfig(subscription="fbfda3f18c634bf6822d8bb8cd301da9", region='eastasia')
    speech_config = speechsdk.SpeechConfig(subscription="d67be56e0dd548eeb0819e937097fd85", region='eastus')
    # In this sample we are using the default speaker
    # Learn how to customize your speaker using SSML in Azure Cognitive Services Speech documentation
    # audio_config = AudioOutputConfig(use_default_speaker=True)
    audio_config = AudioOutputConfig(filename='/home/cmoon/workingspace/src/cmoon/src/c.wav')

    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(
        "Do you need me go to the living room and clean the rubbish there? Please say yes or no.")
    a = synthesizer.speak_text_async(
        "Do you need me go to the living room and clean the rubbish there? Please say yes or no.").get()

    print(a)
    # synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    # result = synthesizer.speak_text_async("Getting the response as an in-memory stream.").get()
    # stream = AudioDataStream(result)


synthesize_to_speaker()
