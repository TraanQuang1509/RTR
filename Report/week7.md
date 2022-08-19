<h1 align="center"> WEEK 7 REPORT </h1> 

## ***Intern: Tran Minh Quang***

> ## **Image Processing**

> ### **1. Introduction to Machine vision**

- Machine vision encompasses all industrial and non-industrial applications in which a combination of hardware and software provide operational guidance to devices in the execution of their functions based on the capture and processing of images.

<div align="center">
    <img src="images/machine_vision.png" width="60%">

*Introduction to Machine vision*
</div>

> ### **2. Introduction to Image Processing**

- Image processing is analyzing and manipulating an image using math
and computer science knowledge.

<div align="center">
    <img src="images/Image_processing.png" width="60%">

*Image Processing*
</div>

- Some applications of Images Processing:

<div align="center">
    <img src="images/self-driving_car.cms" width="60%">

*Computer vision for self-driving car*
</div>

<div align="center">
    <img src="images/reconstruction.jpeg" width="60%">

*Image Reconstruction*
</div>

<div align="center">
    <img src="images/covid_19.png" width="60%">

*Analyze chest X-Rays for signs of Covid-19*
</div>

> ### **3.Image Representation**

- Image as a matrix

    - Digital image is presented by pixel matrix

    - Image processing operation in a computer may be observed as a
    matrix operation

<div align="center">
    <img src="images/pixel_matrix.png" width="60%">

*Image of a character with its pixel intensity values*
</div>

- Color Images
    - Represented by 3 matrices
    
    - Colors are seen as variable combination of primary colors Red (R), Green (G), and blue (B)

    - Each element are integer number range from 0 to 255

    - Intensity of the pixel with respect to the color

    - In RGB system, it’s possible to create 2563=16777216 different
    colors

<div align="center">
    <img src="images/color_image.png" width="60%">
    <img src="images/lena.png" width="60%">

*Color Images*
</div>

- Gray Images

    - Represented by 1 matrix

    - Each element of the matrix is the intensity of the corresponding pixel 

    - Range from 0 (black) to 255 (white)

    - Range from RGB image: Gray = 0.299R + 0.587G + 0.114B

<div align="center">
    <img src="images/gray_img.png" width="60%">
    
*Gray Images*
</div>

- Binary Images

    - Also called Boolean images

    - Represented by a matrix

    - All elements are 0 and 1: 0 is black, 1 is white

    - Result of thresholding operations

    - Important in segmentation

<div align="center">
    <img src="https://media.springernature.com/lw685/springer-static/image/chp%3A10.1007%2F978-3-030-01812-2_8/MediaObjects/467551_1_En_8_Fig2_HTML.jpg" width="60%">
    
*Binary Images*
</div>

- Common Features in Image processing

    - Basic features: Histogram, Color, Edge, Corner,..

    - Advanced features: Regions (Centroid, size, shape,...), Lines (equations, start/end points, orientation,...), Keypoints (Location, Direction, scale,...)

> ### **4. Introduction to OpenCV**

- OpenCV: Open Source Computer Vision & Machine Learning software library

    - Created in 1999 by Intel

    - Supported from 2008 by Willow Garage

    - Willow Garage also supported the Robotic Operating system (ROS) and Point Cloud Library (PCL)

- OpenCV is a cross-plaform, Available in Windows, Linux, Android, MacOS,...

- OpenCV support a wide range of programming languages: