#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Tomasz Kowalski
# DATE CREATED: 07.02.2022
# REVISED DATE: 16.02.2022
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir, getcwd

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = {}
    # get a list of filenames in a given directory
    filenames = listdir(path=image_dir)
    for image_name in filenames:
        # check if procesed file is not a hidden one 
        if image_name[0] != '.':
          # parse image label
          label = image_name[:image_name.index('.')].lower().replace('_', ' ').split()
          for word in label:
              if word.isdigit():
                  label.pop(label.index(word))
          # add image label to results dictionary
          if image_name not in results_dic:
              results_dic[image_name] = [' '.join(label)]
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic


if __name__ == '__main__':
    print(20*'#')
    dir = getcwd()
    print('Current working directory: {}'.format(dir))
    pet_labels = get_pet_labels(dir+'/pet_images')
    for pet in pet_labels.items():
        print('\nFilename= {}, Label ={}'.format(pet[0], pet[1]))
