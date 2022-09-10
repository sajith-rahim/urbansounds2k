
 **urbansounds2k**
 
*2k stratified subset of UrbanSounds8k Dataset.*

<p>


<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" />


## Description

This dataset contains 2000 labeled sound excerpts (<=4s) of urban sounds from 10 classes: air_conditioner, car_horn, 
children_playing, dog_bark, drilling, engine_idling, gun_shot, jackhammer, siren, and street_music. This was extracted from <a href="https://urbansounddataset.weebly.com/urbansound8k.html" target="_blank">UrbanSounds8k</a> dataset as a stratified subset of each class with 200 samples per class.

### Download



### Metadata

File: `urbansounds2k.csv`

| class | class | count | sample |
|-------|-------|-------|--------|
|   0    |  air_conditioner     |   200    |     .   |
|   1    |    car_horn   |    200   |    .    |
|   2   |    children_playing   |    200   |        |
|   3   |    dog_bark   |    200   |        |
|   4   |    drilling   |    200   |        |
|   5    |   engine_idling    |   200    |        |
|   6    |   gun_shot    |   200    |        |
|   7    |   jackhammer    |   200    |        |
|   8    |   siren    |   200    |        |
|   9    |   street_music    |  200     |        |


## UrbanSounds8K
`J. Salamon, C. Jacoby and J. P. Bello, "A Dataset and Taxonomy for Urban Sound Research", 
22nd ACM International Conference on Multimedia, Orlando USA, Nov. 2014.`
#### Created By

**Justin Salamon[1,2], Christopher Jacoby[1] and Juan Pablo Bello[1]**

* [1] Music and Audio Research Lab (MARL), New York University, USA
* [2] Center for Urban Science and Progress (CUSP), New York University, USA
---
1. http://serv.cusp.nyu.edu/projects/urbansounddataset
2. http://marl.smusic.nyu.edu/
3. http://cusp.nyu.edu/


**Download** :<a href="https://urbansounddataset.weebly.com/download-urbansound8k.html" target="_blank"> UrbanSound8K</a>


<pre>
Meta-data Files Included
------------------------

UrbanSound8k.csv

This file contains meta-data information about every audio file in the dataset. This includes:

* slice_file_name: 
The name of the audio file. The name takes the following format: [fsID]-[classID]-[occurrenceID]-[sliceID].wav, where:
[fsID] = the Freesound ID of the recording from which this excerpt (slice) is taken
[classID] = a numeric identifier of the sound class (see description of classID below for further details)
[occurrenceID] = a numeric identifier to distinguish different occurrences of the sound within the original recording
[sliceID] = a numeric identifier to distinguish different slices taken from the same occurrence

* fsID:
The Freesound ID of the recording from which this excerpt (slice) is taken

* start
The start time of the slice in the original Freesound recording

* end:
The end time of slice in the original Freesound recording

* salience:
A (subjective) salience rating of the sound. 1 = foreground, 2 = background.

* fold:
The fold number (1-10) to which this file has been allocated.

* classID:
A numeric identifier of the sound class:
0 = air_conditioner
1 = car_horn
2 = children_playing
3 = dog_bark
4 = drilling
5 = engine_idling
6 = gun_shot
7 = jackhammer
8 = siren
9 = street_music

* class:
The class name: air_conditioner, car_horn, children_playing, dog_bark, drilling, engine_idling, gun_shot, jackhammer, 
siren, street_music.


Please Acknowledge UrbanSound8K in Academic Research
----------------------------------------------------

When UrbanSound8K is used for academic research, we would highly appreciate it if scientific publications of works 
partly based on the UrbanSound8K dataset cite the following publication:

J. Salamon, C. Jacoby and J. P. Bello, "A Dataset and Taxonomy for Urban Sound Research", 
22nd ACM International Conference on Multimedia, Orlando USA, Nov. 2014.

The creation of this dataset was supported by a seed grant by NYU's Center for Urban Science and Progress (CUSP).


Conditions of Use
-----------------

Dataset compiled by Justin Salamon, Christopher Jacoby and Juan Pablo Bello. All files are excerpts of recordings
uploaded to www.freesound.org. Please see FREESOUNDCREDITS.txt for an attribution list.
 
The UrbanSound8K dataset is offered free of charge for non-commercial use only under the terms of the Creative Commons
Attribution Noncommercial License (by-nc), version 3.0: http://creativecommons.org/licenses/by-nc/3.0/
 
The dataset and its contents are made available on an "as is" basis and without warranties of any kind, including 
without limitation satisfactory quality and conformity, merchantability, fitness for a particular purpose, accuracy or 
completeness, or absence of errors. Subject to any liability that may not be excluded or limited by law, NYU is not 
liable for, and expressly excludes, all liability for loss or damage however and whenever caused to anyone by any use of
the UrbanSound8K dataset or any part of it.
</pre>

