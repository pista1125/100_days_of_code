# from os import path
# from pydub import AudioSegment
#
# # # files
# # src = "horvath.mp3"
# # dst = "test.wav"
# #
# # # convert wav to mp3
# # sound = AudioSegment.from_mp3(src)
# # sound.export(dst, format="wav")
#
# # import required modules
# import subprocess
#
# # convert mp3 to wav file
# subprocess.call(['ffmpeg', '-i', 'horvath.mp3',
#                  'converted_to_wav_file.wav'])
# import time
#
# game = True
# x = 0
# for x in range(100):
#     number = str(2**x)
#
#     print(f"{number}-->{x}-->{len(number)}")

game = [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]

move_1 = 1
move_2 = 2
move_3 = 3
move_5 = 5
for x in range(5):
    game.append(0)

move = 0

move_list = [1]

position = 0
while position != len(game) - 6:
    if game[position + move_5] == 1:
        position += move_5
        move_list.append(position + 1)
        move += 1
    if game[position + move_3] == 1:
        position += move_3
        move_list.append(position + 1)
        move += 1
    if game[position + move_2] == 1:
        position += move_2
        move_list.append(position + 1)
        move += 1
    if game[position + move_1] == 1:
        position += move_1
        move_list.append(position + 1)
        move += 1

print(move)
print(move_list)






