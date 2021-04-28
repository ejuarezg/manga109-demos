# Manga109 Demos

This repository is a collection of demo codes for the [Manga109 dataset](http://www.manga109.org/en/).

Manga109 is the largest dataset for manga (Japanese comic) images,
that is made publicly available for academic research purposes with proper copyright notation.

To download images/annotations of Manga109, please visit [this website](http://www.manga109.org/en/download.html) and send an application via the form.
You will then receive a password for downloading the images (109 titles of manga
as jpeg files)
and their annotations (bounding box coordinates of face, body, frame, and speech balloon with texts,
in the form of XML).

Please see [manga109api](https://github.com/manga109/manga109api) as well when using the dataset.

## Contents

- Annotation visualization demo - `./visualization`
- Bounding box cropping demo - `./extraction`


## Scripts for use with SSD300

The script `./ssd300_use/create_pickle_file.py` generates a pickle file with bounding box annotations of speech balloons in every page containing balloons. This pickle file is specifically formatted to be used in the SSD300 neural network implementation provided in https://github.com/ejuarezg/SSD300.

After generating the `Manga109.pkl` file, place it in the root of the SSD300 repo.

## Citations
When you make use of images in Manga109, please cite the following paper:

    @article{mtap_matsui_2017,
        author={Yusuke Matsui and Kota Ito and Yuji Aramaki and Azuma Fujimoto and Toru Ogawa and Toshihiko Yamasaki and Kiyoharu Aizawa},
        title={Sketch-based Manga Retrieval using Manga109 Dataset},
        journal={Multimedia Tools and Applications},
        volume={76},
        number={20},
        pages={21811--21838},
        doi={10.1007/s11042-016-4020-z},
        year={2017}
    }

When you use annotation data of Manga109, please cite the following paper:

    @article{multimedia_aizawa_2020,
        author={Kiyoharu Aizawa and Azuma Fujimoto and Atsushi Otsubo and Toru Ogawa and Yusuke Matsui and Koki Tsubota and Hikaru Ikuta},
        title={Building a Manga Dataset ``Manga109'' with Annotations for Multimedia Applications},
        journal={IEEE MultiMedia},
        volume={27},
        number={2},
        pages={8--18},
        doi={10.1109/mmul.2020.2987895},
        year={2020}
    }
