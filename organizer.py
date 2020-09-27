import os
import sys
from pprint import pprint
import shutil
from pathlib import Path
from PyQt5 import QtWidgets, QtCore, QtGui


compressed_files = ['.7z', '.tar', '.cbr', '.deb', '.gz', '.pkg',
                    '.rar', '.rpm', '.sitx', '.tar.gz', '.zip', '.zipx', '.tar.bz2']
document_files = ['.doc', '.docx', '.log', '.msg', '.odt', '.pages', '.rtf', '.tex', '.tiff', '.txt', '.wpd', '.wps',
                  '.csv', '.dat', '.ged', '.key', '.keychain', '.pps', '.ppt', '.pptx', '.sdf', '.tar', '.tax2016', '.tax2019', '.vcf', '.xml',
                  '.xlr', '.xls', '.xlsx', '.indd', '.pct', '.pdf']
audio_files = ['.aif', '.iff', '.m3u', '.m4a',
               '.mid', '.mp3', '.mpa', '.wav', '.wma']
video_files = ['.3g2', '.3gp', '.asf', '.avi', '.flv', '.m4v', '.mov',
               '.mp4', '.mpg', '.rm', '.srt', '.swf', '.vob', '.wmv', '.webm']
image_files = ['.3dm', '.3ds', '.max', '.obj', '.bmp', '.dds', '.gif', '.heic', '.jpg', '.png', '.psd', '.pspimage', '.tga', '.thm', '.yuv',
               '.ai', '.eps', '.svg', '.jpeg']
developer_files = ['.c', '.class', '.cpp', '.cs', '.dtd', '.fla', '.h', '.java', '.lua', '.m', '.pl', '.py', '.sh', '.sln',
                   '.swift', '.vb', '.vcxproj', '.xcodeproj', '.dwg', '.dxf', '.accdb', '.db', '.dbf', '.mdb', '.pdb', '.sql', '.asp', '.aspx',
                   '.cer', '.cfm', '.csr', '.css', '.dcr', '.htm', '.html', '.js', '.jsp', '.php', '.rss', '.xhtml', '.crx', '.plugin',
                   '.fnt', '.fon', '.otf', '.ttf', '.xcf']
misc_files = []


def organize(extension_list, file_name, old_path, new_path):
    for file_type in extension_list:
        if file_type in file_name:
            # print("found")
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            try:
                shutil.copy(str(old_path), str(new_path))
                os.remove(str(old_path))
            except:
                return


def main():
	app = QtWidgets.QApplication(sys.argv)

	dialog = QtWidgets.QFileDialog()
	directory = Path(dialog.getExistingDirectory(None, 'Select a directory to organize'))

	if str(directory) != '.':
		files_to_organize = os.listdir(directory)


		if not os.path.exists(directory.joinpath('Organized Folder')):
			os.mkdir(directory.joinpath('Organized Folder'))

		for file in files_to_organize:
			organize(compressed_files, file, directory.joinpath(file), directory.joinpath('Organized Folder', 'Compressed Files'))
			organize(document_files, file, directory.joinpath(file), directory.joinpath('Organized Folder', 'Document Files'))
			organize(audio_files, file, directory.joinpath(file),directory.joinpath('Organized Folder', 'Audio Files'))
			organize(video_files, file, directory.joinpath(file),directory.joinpath('Organized Folder', 'Video Files'))
			organize(image_files, file, directory.joinpath(file),directory.joinpath('Organized Folder', 'Image Files'))
			organize(developer_files, file, directory.joinpath(file), directory.joinpath('Organized Folder', 'Developer Files'))
			organize(misc_files, file, directory.joinpath(file),directory.joinpath('Organized Folder', 'Misc Files'))

if __name__ == "__main__":
	main()