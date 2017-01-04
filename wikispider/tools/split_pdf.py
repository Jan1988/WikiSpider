import os
import time

from PyPDF2 import PdfFileWriter, PdfFileReader


# default input file_path_in is the
def split_single_pdf(filename, file_path_in, file_path_out):

    print(file_path_in)

    pages_created = 0
    if filename.endswith(".pdf"):

        try:
            print('PDF file ' + filename + ' is processed')

            filename_no_suffix = filename.replace('.pdf', '')
            file_in = file_path_in + filename

            opened_file = PdfFileReader(open(file_in, "rb"))

            for i in range(opened_file.numPages):
                output = PdfFileWriter()
                output.addPage(opened_file.getPage(i))

                output_file = file_path_out + filename_no_suffix + '_page_%s.pdf' % i

                with open(output_file, "wb") as outputStream:
                    output.write(outputStream)
                    pages_created += 1

        except:  # catch *all* exceptions
            # os.remove(output_file)
            print('_______' + filename + ' was not completely split_______')

    print('Pages created: ' + str(pages_created))
    return pages_created




# Input Folder where pdf tools are located
folder_path_in = os.path.join('Assets', '')




