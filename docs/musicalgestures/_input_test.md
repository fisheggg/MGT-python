# Input Test

> Auto-generated documentation for [musicalgestures._input_test](https://github.com/fourMs/MGT-python/blob/master/musicalgestures/_input_test.py) module.

- [Mgt-python](../README.md#mgt-python) / [Modules](../MODULES.md#mgt-python-modules) / [Musicalgestures](index.md#musicalgestures) / Input Test
    - [Error](#error)
    - [InputError](#inputerror)
    - [mg_input_test](#mg_input_test)

## Error

[[find in source code]](https://github.com/fourMs/MGT-python/blob/master/musicalgestures/_input_test.py#L3)

```python
class Error(Exception):
```

Base class for exceptions in this module.

## InputError

[[find in source code]](https://github.com/fourMs/MGT-python/blob/master/musicalgestures/_input_test.py#L8)

```python
class InputError(Error):
    def __init__(message):
```

Exception raised for errors in the input.

#### Arguments

- `Error` *str* - Explanation of the error.

#### See also

- [Error](#error)

## mg_input_test

[[find in source code]](https://github.com/fourMs/MGT-python/blob/master/musicalgestures/_input_test.py#L20)

```python
def mg_input_test(
    filename,
    array,
    fps,
    filtertype,
    thresh,
    starttime,
    endtime,
    blur,
    skip,
    frames,
):
```

Gives feedback to user if initialization from input went wrong.

#### Arguments

- `filename` *str* - Path to the input video file.
- `array` *np.ndarray, optional* - Generates an MgVideo object from a video array. Defauts to None.
- `fps` *float, optional* - The frequency at which consecutive images from the video array are captured or displayed. Defauts to None.
- `filtertype` *str* - 'Regular' turns all values below `thresh` to 0. 'Binary' turns all values below `thresh` to 0, above `thresh` to 1. 'Blob' removes individual pixels with erosion method.
- `thresh` *float* - A number in the range of 0 to 1. Eliminates pixel values less than given threshold.
- `starttime` *int/float* - Trims the video from this start time (s).
- `endtime` *int/float* - Trims the video until this end time (s).
- `blur` *str* - 'Average' to apply a 10px * 10px blurring filter, 'None' otherwise.
- `skip` *int* - Every n frames to discard. `skip=0` keeps all frames, `skip=1` skips every other frame.
- `frames` *int* - Specify a fixed target number of frames to extract from the video.

#### Raises

- `InputError` - If the types or options are wrong in the input.
