import os, time, subprocess

series = ['01. Série', '02. Série']

path = "E:\\Serialy\\M'A'S'H - 1. - 11. Série (DVD-Rip) + MASH (DVD-Full)"

destination_folder = 'libx265'

output_video_container = '.mkv'  # # or .mp4
# https://en.wikipedia.org/wiki/Matroska

for seria in series:

	working_path = os.path.join(path, seria)
	print(working_path)

	for root, dirs, files in os.walk(working_path, topdown=False):
		for name in files:

			# # --- original file with path
			input_file = os.path.join(root, name)
			print(f'Input file: {input_file}')

			# # --- build destination folder
			root_path = '\\'.join(root.split('\\')[:-1])
			sub_folder = root.split('\\')[-1:]

			full_path_output = os.path.join(root_path, destination_folder, sub_folder[0])

			# # --- we must create destination folder
			if not os.path.exists(full_path_output):
				os.makedirs(full_path_output)

			# # --- final file with path
			name = name.split('.')[:-1]  # # cut off original suffix
			name = '.'.join(name) + output_video_container  # # and we paste our prefer video format
			output_file = os.path.join(full_path_output, name)
			print(f'Output file: {output_file}')

			# # --- ' and " makes problems in ffmpeg command line
			input_file = input_file.replace("'", "\'")
			input_file = input_file.replace('"', '\"')

			output_file = output_file.replace("'", "\'")
			output_file = output_file.replace('"', '\"')

			# # --- calling ffmpeg https://ffmpeg.org/ https://en.wikipedia.org/wiki/FFmpeg
			ffmpeg_cli = "ffmpeg -i \"{}\" -vcodec libx265 \"{}\"".format(input_file, output_file)
			subprocess.call(ffmpeg_cli, shell=True)

			# cooling CPU
			time.sleep(60)
			
