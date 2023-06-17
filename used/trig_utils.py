import cv2

def overlay_top_left(background, overlay):
    gen_over_lay(background, overlay, x=0, y=0)


def overlay_bottom_right(background, overlay):

    roi_y_start = background.shape[1] - overlay.shape[1]
    roi_x_start = background.shape[0] - overlay.shape[0]

    gen_over_lay(background, overlay, x=roi_x_start, y=roi_y_start)

# def gen_over_lay(background, overlay, x, y):
#     """
#     :param background:
#     :param overlay:
#     :param x: x-coordinate of the top-left corner of the overlay image
#     :param y: y-coordinate of the top-left corner of the overlay image
#     :return: None
#     """
#
#     # Determine the dimensions of the overlay image
#     overlay_height, overlay_width, _ = overlay.shape
#
#     # Calculate the region of interest (ROI) coordinates
#     roi_y_start = y
#     roi_y_end = y + overlay_height
#     roi_x_start = x
#     roi_x_end = x + overlay_width
#
#     # Extract the ROI from the background image
#     roi = background[roi_y_start:roi_y_end, roi_x_start:roi_x_end]
#
#     # Perform the overlay by blending the images within the ROI
#
#     result = cv2.addWeighted(roi, 0, overlay, 1, 0)
#
#     # Replace the ROI in the background image with the overlay
#     background[roi_y_start:roi_y_end, roi_x_start:roi_x_end] = result

def gen_over_lay(background, overlay, x, y):
    """
    :param background:
    :param overlay:
    :param x: x-coordinate of the top-left corner of the overlay image
    :param y: y-coordinate of the top-left corner of the overlay image
    :return: None
    """

    # Determine the dimensions of the overlay image
    overlay_height, overlay_width, _ = overlay.shape

    # Calculate the region of interest (ROI) coordinates
    roi_y_start = y
    roi_y_end = y + overlay_height
    roi_x_start = x
    roi_x_end = x + overlay_width

    # Extract the ROI from the background image
    roi = background[roi_y_start:roi_y_end, roi_x_start:roi_x_end]

    # Perform the overlay by blending the images within the ROI

    result = cv2.addWeighted(roi, 0, overlay, 1, 0)

    # Replace the ROI in the background image with the overlay
    background[roi_y_start:roi_y_end, roi_x_start:roi_x_end] = result