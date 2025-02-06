import os
import sys
from pilk import decode
import subprocess

import vosk
import wave
import sys

from vosk import Model, KaldiRecognizer, SetLogLevel
import json



def convert_to_wav(input_file, output_file):
    command = ['ffmpeg', '-i', input_file, '-ac', '1', '-f', 'wav', output_file]

    subprocess.run(command)


def vocie2text_offline(voicepath):


    # You can set log level to -1 to disable debug messages
    SetLogLevel(0)
    # 使用示例
    input_file = voicepath  # 输入文件路径
    output_file = voicepath+".wav"  # 输出文件路径
    convert_to_wav(input_file, output_file)
    wf = wave.open(output_file, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        return "任务失败"

    # model = Model(lang="en-us")
    model_path = "contentgenerate\\vosk-model-small-cn-0.22"  # 替换为你的模型路径
    model = vosk.Model(model_path)


    # You can also init model by name or with a folder path
    # model = Model(model_name="vosk-model-en-us-0.21")
    # model = Model("models/en")

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    rec.SetPartialWords(True)

    all_results = []

    with wave.open(output_file, "rb") as wf:
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            raise ValueError("Audio file must be WAV format mono PCM.")
        
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                # 获取并存储中间结果
                result_dict = json.loads(rec.Result())
                all_results.append(result_dict)
                print("中间结果:", result_dict)

        # # 获取最终结果
        # final_result = json.loads(rec.FinalResult())
        # if final_result:  # 确保final_result不为空
        #     all_results.append(final_result)
        #     print("最终结果:", final_result)

    # 处理all_results列表中的所有结果
    res=""
    for result in all_results:
        res=res+result["text"]

        
        # data = wf.readframes(4000)
        # if len(data) == 0:
        #     break
        # if rec.AcceptWaveform(data):
        #     print(rec.Result())
        # else:
        #     print(rec.PartialResult())
    # result=eval(rec.FinalResult())
    # print(result)
    print(res)
    return res


    
if __name__ == '__main__':
    path="./project/中科蓝吧-script1/中科蓝吧-script1.mp4"
    res=vocie2text_offline(path)
    print(res)