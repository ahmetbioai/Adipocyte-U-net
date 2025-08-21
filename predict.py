import sys, glob, numpy as np, cv2
from keras import backend as K
def metric_wrapper(yt, yp, metric): 
    return K.get_value(metric(K.variable(yt), K.variable(yp)))
if __name__ == "__main__":
    img_dir = sys.argv[1] if len(sys.argv) > 1 else "example_tiles"
    paths = glob.glob(img_dir + "/*")
    print(f"Found {len(paths)} images in {img_dir}")
