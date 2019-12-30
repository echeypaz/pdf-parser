# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
import os
#import csv
import PyPDF2
import re
import sys
# import HttpResponse
import googleclouddebugger
googleclouddebugger.enable()

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    
    
    
    """Return a friendly HTTP greeting."""

    # with open('/tmp/resulst.csv', 'w', newline='') as csvfile:
    #    quoting_ = csv.QUOTE_MINIMAL
    #    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|',
    #                            quoting=quoting_)
    #    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    #    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    # response = HttpResponse(csvfile.getvalue(), content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename=stock.csv'
    # return response
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files = filter(lambda f: f.endswith(('.pdf', '.PDF')), files)
    doc_types = ["Notas de lectura", "notas digitales", "monografias", "noticias", "articulos"]
    abstract_types = ["Resumen", "Abstract", "Resumé"]
    keywords_types = ["Palabras Clave", "Key Words", "Mots clé"]

    for doc in files:
        pdfFileObj = open(doc, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        content = ""
        for page in pdfReader.pages:
            content = content + str(page.extractText())
            for doc_type in doc_types:
                patron = re.compile('(.*)?' + doc_type)
                for search in patron.finditer(content):
                    # sys.stdout.write(search)
                    sys.stdout.write("********************************")

    return content


if __name__ == '__main__':
    # print(hello())
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='0.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
