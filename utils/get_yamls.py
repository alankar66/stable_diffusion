import sys
import requests,yaml

_V2V_URL = ["v2-inference-v_new.yaml","https://github.com/Stability-AI/stablediffusion/blob/main/configs/stable-diffusion/v2-inference-v.yaml"]
_V2_URL = ["v2-inference_new.yaml","https://github.com/Stability-AI/stablediffusion/blob/main/configs/stable-diffusion/v2-inference.yaml"]
_V1_URL = ["v1-inference_new.yaml","https://github.com/CompVis/stable-diffusion/blob/main/configs/stable-diffusion/v1-inference.yaml"]

def download_all():
    list = [_V2V_URL,_V2_URL,_V1_URL]
    for file in list:
        get_yaml(file)


def get_yaml(file):
    res = requests.request(method="GET", url=file[1])
    print(res.content)
    with open(file[0],"w") as f:
        # f.write(res.content)
        yaml.dump(res.content,f)
    print(f" downloaded: {file[0]}")

if __name__ == '__main__':
    download_all()
    print("SD1.x and SD2.x yamls downloaded")
