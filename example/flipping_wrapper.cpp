#include "flipping_wrapper.h"
#include "some_project/flipping.h"


CV_EXPORTS_W void flipping::vertflip(cv::InputArray img_, cv::OutputArray flipped_) {
    // Convert arguments, make copies where necessary
    cv::Mat img = img_.getMat();
    cv::Mat flipped;
    // Actual call to the original function. If your wrapped function has the 
    // same name, don't forget the :: to avoid calling the current function 
    // again.
    ::vertflip(img, flipped);
    flipped_.assign(flipped);
}


CV_EXPORTS_W void flipping::hzflip(cv::InputArray img_, cv::OutputArray flipped_) {
    cv::Mat img = img_.getMat();
    cv::Mat flipped;
    ::hzflip(img, flipped);
    flipped_.assign(flipped);
}
