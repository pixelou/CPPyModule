#include <opencv2/core.hpp>

namespace flipping {

CV_EXPORTS_W void vertflip(cv::InputArray img, cv::OutputArray flipped);

CV_EXPORTS_W void hzflip(cv::InputArray img, cv::OutputArray flipped);

}
