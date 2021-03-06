from modules.watson_developer_cloud import VisualRecognitionV3
from operator import itemgetter
from io import BytesIO, StringIO
from PIL import Image
import base64


class ImageClasses:
    """
    :param str image_url: A string with the image URL to analyze. Must be in .jpg, or .png format. The minimum recommended pixel density is 32X32 pixels per inch, and the maximum image size is 10 MB. You can also include images in the **images_file** parameter.
    :param string threshold: A floating point value that specifies the minimum score a class must have to be displayed in the response. The default threshold for returning scores from a classifier is `0.5`. Set the threshold to `0.0` to ignore the classification score and return all values.
    """

    def __init__(self, image_url=None, threshold="0.5"):
        self.image_url = image_url
        self.threshold = threshold
        self.classes = self.getClasses()

    def getClasses(self):
        return [{"score":0.97,"class":"apple"},{"score":0.97,"class":"fruit"},{"score":0.97,"class":"accessory fruit"},{"score":0.97,"class":"dessert apple"}]
        vision = VisualRecognitionV3(
            api_key="55756fcdc3bc6672c581812037e7296e3d74f396",
            version="2018-03-19"
        )
        decode_str = base64.b64decode(self.image_url.encode('ascii'))
        file_like = BytesIO(decode_str)
        img = Image.open(file_like)


        #if "http" not in self.image_url:
        #img = base64.decodestring(self.image_url.encode('ascii'))
        with open('static/images/test.jpg','wb') as fh:
            fh.write(base64.decodebytes(img))

            response = vision.classify(images_file=fh,
                                   threshold=self.threshold,
                                   accept_language="en",
                                   classifier_ids=["food"],
                                   owners=["IBM"])

        #with open('static/images/test.jpg', 'rb') as f:
        #    response = vision.classify(images_file=f,
        #                               threshold=self.threshold,
        #                               accept_language="en",
        #                               classifier_ids=["food"],
        #                               owners=["IBM"])
        #else:
            response = vision.classify(url=self.image_url,
                                       threshold=self.threshold,
                                       accept_language="en",
                                       classifier_ids=["food"],
                                       owners=["IBM"])

        dictionaryList = response["images"][0]["classifiers"][0]["classes"]
        return sorted(dictionaryList, key=itemgetter("score"), reverse=True)
