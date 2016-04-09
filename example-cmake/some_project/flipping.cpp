#include "flipping.h"

using namespace cv;

void vertflip(const cv::Mat& in, cv::Mat& out) {
    flip(in, out, 0);
}

void hzflip(const cv::Mat& in, cv::Mat& out) {
    flip(in, out, 1);
}
