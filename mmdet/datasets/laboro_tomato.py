from .coco import CocoDataset
from .builder import DATASETS
dataset_type = 'CocoDataset'
_base_ = 'coco_instance.py'

@DATASETS.register_module()
class LaboroTomato(CocoDataset):
    CLASSES = ('b_fully_ripened', 'b_half_ripened', 'b_green', 
               'l_fully_ripened', 'l_half_ripened', 'l_green')

    data = dict(
        samples_par_gpu=2,
        workers_par_gpu=2,
        train=dict(
            type=dataset_type,
            classes=CLASSES,  # COCOデータセットのクラスをオーバーライド
            ann_file='data/labro_tomato/annotations/instances_train2017.json',
            img_prefix='data/laboro_tomato/train2017'),
        val=dict(
            type=dataset_type,
            classes=CLASSES,  # COCOデータセットのクラスをオーバーライド
            ann_file='data/labro_tomato/annotations/instances_test2017.json',
            img_prefix='data/laboro_tomato/test2017'),
        test=dict(
            type=dataset_type,
            classes=CLASSES,  # COCOデータセットのクラスをオーバーライド
            ann_file='data/labro_tomato/annotations/instances_test2017.json',
            img_prefix='data/laboro_tomato/test2017')
    )
