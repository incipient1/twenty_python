import pyaudio,aip

import wave,win32api

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
RECORD_SECOND = 3
WAVE_OUTPUT_FILENAME = "out.wav"

def make_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format = FORMAT,
        channels = CHANNELS,
        rate = RATE,
        input = True,
        frames_per_buffer = CHUNK)
    print('*recording')
    frames = []
    for i in range(0,int(RATE / CHUNK * RECORD_SECOND)):
        data = stream.read(CHUNK)
        frames.append(data)
    print('*done')
    stream.stop_stream()
    stream.close()
    wf = wave.open(WAVE_OUTPUT_FILENAME,'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def speech_to_text():
    app_id = '10488070'
    api_key = '9SupHA6M6KYjaA60wbTf0CEp'
    secret_key = '42689bb0b63888aa8421cd760d3c7fbe'
    aipspeech = aip.AipSpeech(app_id,api_key,secret_key)
    speech_content = aipspeech.asr(open(WAVE_OUTPUT_FILENAME,'rb').read(),
        'wav',RATE,{'lan':'zh'})
    speech_result_str = ''
    for i in speech_content['result']:
        speech_result_str += i
    print(speech_result_str)
    return speech_result_str

def take_action(texts):
    maps = {'百度':'https://www.baidu.com',
    '必应':'https://cn.bing.com'}
    target = ''
    for text in texts:
        if '百度' in texts or 'baidu' in texts:
            target = '百度'
        if '必应' in  texts:
            target = '必应'

    if target:
        win32api.ShellExecute(0,'open',maps[target],'','',1)
    else:
        print('match failed:','texts')

if __name__ == "__main__":
    make_audio()
    texts = speech_to_text()
    take_action(texts)