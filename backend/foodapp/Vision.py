from watson_developer_cloud import VisualRecognitionV3
from operator import itemgetter


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
        vision = VisualRecognitionV3(
            api_key="55756fcdc3bc6672c581812037e7296e3d74f396",
            version="2018-03-19"
        )

        with open(self.image_url, 'rb') as f:
            response = vision.classify(images_file=f,
                                       threshold=self.threshold,
                                       accept_language="en",
                                       classifier_ids=["food"],
                                       owners=["IBM"])

        dictionaryList = response["images"][0]["classifiers"][0]["classes"]
        return sorted(dictionaryList, key=itemgetter("score"), reverse=True)
