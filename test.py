import urllib.request
import requests
import os
import json

# output_dir = './static'

# def download_file_from_api(output_dir, data_url):

#     # Make output directory if not exist
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     # save path
#     image_save_path = output_dir + os.sep + os.path.basename(data_url)

#     # Download file from url
#     urllib.request.urlretrieve(data_url, image_save_path)

#     print(image_save_path)


# with urllib.request.urlopen("http://192.168.69.226:3000/upload/getlink/twitter") as url:
#     my_bytes_value = url.read()
#     # I'm guessing this would output the html source code ?
#     print(type(my_bytes_value))
#     # Decode UTF-8 bytes to Unicode, and convert single quotes 
#     # to double quotes to make it valid JSON
#     my_json = my_bytes_value.decode('utf8').replace("'", '"')

#     # Load the JSON to a Python list & dump it back out as formatted JSON
#     data = json.loads(my_json)
#     s = json.dumps(data, indent=4, sort_keys=True)
#     dictionary = json.loads(s)
#     print(dictionary['fset'])
#     download_file_from_api(output_dir, dictionary['fset'])
#     download_file_from_api(output_dir, dictionary['fset3'])
#     download_file_from_api(output_dir, dictionary['iset'])


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

name_type = 'n_video'
name_all_videos = processing_one_type("http://192.168.69.108:3000/getcontent/videoasset", name_type)
print(name_all_videos)

output_dir = './static/videos'

def download_file_from_api(output_dir, data_url):
    # Make output directory if not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # save path
    save_path = output_dir + os.sep + os.path.basename(data_url)
    # Download file from url
    urllib.request.urlretrieve(data_url, save_path)
    print(save_path)


def processing(link_name, name_video):
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

name_video = '5540148773739827724.mp4'
video = processing("http://192.168.69.108:3000/getcontent/videoasset", name_video)
download_file_from_api(output_dir, video)
# print(name_video.split('.')[0])

# import urllib.request
# import os

# output_dir = './static'
# image_url = 'https://vinasupport.com/assets/img/vinasupport_logo.png'

# # Make output directory if not exist
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# # save path
# image_save_path = output_dir + '/' + os.path.basename(image_url)

# # Download file from url
# urllib.request.urlretrieve(image_url, image_save_path)
# print(image_save_path)

