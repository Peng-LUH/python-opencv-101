def add(a: float, b: float) -> float:
    return a + b


def greeting(name: str) -> str:
    name = name.strip()
    if not name:
        return "Hello!"
    return f"Hello, {name}!"


import cv2 as cv
from cv2.typing import MatLike
from typing import Optional

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