from django.shortcuts import render
import urllib.request
import requests
import os
import json

ip = "192.168.0.134"
# Create your views here.
output_dir_image = './static/images'
output_dir_video = './static/videos'

def download_file_from_api(output_dir, data_url):
    # Make output directory if not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # save path
    save_path = output_dir + os.sep + os.path.basename(data_url)
    # Download file from url
    urllib.request.urlretrieve(data_url, save_path)
    print(save_path)

def processing(link_name, name_image):
    with urllib.request.urlopen(link_name) as url:
        my_bytes_value = url.read()
        # I'm guessing this would output the html source code ?
        print(type(my_bytes_value))
        # Decode UTF-8 bytes to Unicode, and convert single quotes 
        # to double quotes to make it valid JSON
        my_json = my_bytes_value.decode('utf8').replace("'", '"')
        print(type(my_json))
        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        s = json.dumps(data, indent=4, sort_keys=True)
        print(type(s))
        dictionary = json.loads(s)
        for file_dic in dictionary:
            print(file_dic['n_image'].split('.'))
            print(name_image)
            if file_dic['n_image'] == name_image:
                # print(file_dic['id'])
                # print(file_dic['n_image'])
                # print(file_dic['l_image'])
                print(file_dic['l_nft'])
                return file_dic['l_nft']

def processing_file(link_name):
    with urllib.request.urlopen(link_name) as url:
        my_bytes_value = url.read()
        # I'm guessing this would output the html source code ?
        print(type(my_bytes_value))
        # Decode UTF-8 bytes to Unicode, and convert single quotes 
        # to double quotes to make it valid JSON
        my_json = my_bytes_value.decode('utf8').replace("'", '"')

        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        s = json.dumps(data, indent=4, sort_keys=True)
        dictionary = json.loads(s)
        print(dictionary['fset'])
        download_file_from_api(output_dir_image, dictionary['fset'])
        download_file_from_api(output_dir_image, dictionary['fset3'])
        download_file_from_api(output_dir_image, dictionary['iset'])

# Tùy chọn vào kiểu
def processing_one_type(link_name, name_type):
    with urllib.request.urlopen(link_name) as url:
        my_bytes_value = url.read()
        # I'm guessing this would output the html source code ?
        print(type(my_bytes_value))
        # Decode UTF-8 bytes to Unicode, and convert single quotes 
        # to double quotes to make it valid JSON
        my_json = my_bytes_value.decode('utf8').replace("'", '"')
        print(type(my_json))
        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        s = json.dumps(data, indent=4, sort_keys=True)
        print(type(s))
        dictionary = json.loads(s)
        list_result = []
        for file_dic in dictionary:
            list_result.append(file_dic[str(name_type)])
        return list_result

def processing_video(link_name, name_video):
    with urllib.request.urlopen(link_name) as url:
        my_bytes_value = url.read()
        # I'm guessing this would output the html source code ?
        print(type(my_bytes_value))
        # Decode UTF-8 bytes to Unicode, and convert single quotes 
        # to double quotes to make it valid JSON
        my_json = my_bytes_value.decode('utf8').replace("'", '"')
        print(type(my_json))
        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        s = json.dumps(data, indent=4, sort_keys=True)
        print(type(s))
        dictionary = json.loads(s)
        for file_dic in dictionary:
            print(file_dic['n_video'].split('.'))
            print(name_video)
            if file_dic['n_video'] == name_video:
                return file_dic['l_video']

def processing_file_video(list_):
    return ""

def index(request):
    name_type = 'n_image'
    name_all_images = processing_one_type("http://" + ip + ":3000/getcontent/imgasset", name_type)
    print(name_all_images)
    context = {
        'name_all_images':name_all_images
    }
    return render(request, 'index.html', context=context)

def upload_image(request):
    context = {
        'name_page':'hình ảnh',
        'type':'image',
        'ip_host':ip
    }
    return render(request, 'upload.html', context=context)

def select_video(request):
    name_type = 'n_video'
    name_all_videos = processing_one_type("http://" + ip + ":3000/getcontent/videoasset", name_type)
    print(name_all_videos)
    context = {
        'name_all_videos':name_all_videos
    }
    return render(request, 'index_video.html', context=context)

def upload_video(request):
    context = {
        'name_page':'video',
        'type':'video',
        'ip_host':ip
    }
    return render(request, 'upload.html', context=context) 

def result(request):
    name_image = request.POST['NAME_IMAGE']
    image = processing("http://" + ip + ":3000/getcontent/imgasset", name_image)
    processing_file(image)
    print(name_image.split('.')[0])

    # name_video = request.POST['NAME_VIDEO']
    name_video = 'videodemo.mp4'
    video = processing_video("http://" + ip + ":3000/getcontent/videoasset", name_video)
    download_file_from_api(output_dir_video, video)
    print(name_video.split('.')[0])

    context = {
        'name_file_image': name_image.split('.')[0],
        # 'name_file_video': name_video
    }
    return render(request, 'result.html', context=context)
