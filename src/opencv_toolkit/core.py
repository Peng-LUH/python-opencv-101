from typing import Optional

import cv2 as cv
from cv2.typing import MatLike


def add(a: float, b: float) -> float:
    return a + b


def greeting(name: str) -> str:
    name = name.strip()
    if not name:
        return "Hello!"
    return f"Hello, {name}!"


def rescale_frame(frame: Optional[MatLike], scale: float) -> Optional[MatLike]:
    """rescale an image

    Returns `None` if `frame` is `None`.
    """
    if frame is None:
        return None

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# def change_resolution(width: int, height: int):
#     """
#     change the resolution for live videos

#     :param width: Description
#     :type width: int
#     :param height: Description
#     :type height: int
#     """
#     capture.set(3, width)
#     capture.set(4, height)
