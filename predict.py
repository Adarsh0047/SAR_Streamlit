from mmdet.apis import DetInferencer
import glob
import warnings
import boto3
warnings.filterwarnings('ignore')
import os

def predict(img):
    # print(img)
    ext = img.split(".")[1]
    # print(ext)
    model_name = 'tood_r50_fpn_1x_coco'
    # Setup a checkpoint file to load

    checkpoint = 'best_coco_bbox_mAP_epoch_12.pth'
    if not os.path.exists(checkpoint):
        s3 = boto3.resource('s3', region_name='ap-south-1')
        bucket = s3.Bucket('sar-models')
        object = bucket.Object('best_coco_bbox_mAP_epoch_12.pth')
        object.download_file('best_coco_bbox_mAP_epoch_12.pth')
    # Set the device to be used for evaluation
    device = 'cpu'

    # Initialize the DetInferencer
    inferencer = DetInferencer(model_name, checkpoint, device)
    _ = inferencer(img, out_dir="result/")
    paths = glob.glob(f"result/vis/*.{ext}")
    print(paths)
    for path in paths:
        if path.split("/")[-1] == img:
            return path
