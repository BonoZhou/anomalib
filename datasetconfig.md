```yaml
dataset:  
  name: cpu #dataset name
  format: folder #folder,一般不改
  path: ./datasets/CPU #dataset路径
  task: classification #分为classification detection segmentation
  normal_dir: "OK1" #正常数据集
  normal_test_dir: #不填留空
  abnormal_dir: "NG1" #异常数据集
  mask_dir:    #mask数据集
  extensions: ".jpg" #图片格式
  train_batch_size: 32
  eval_batch_size: 32
  num_workers: 8
  image_size: 256 # dimensions to which images are resized (mandatory)
  center_crop: 224 # dimensions to which images are center-cropped after resizing (optional)
  normalization: imagenet # data distribution to which the images will be normalized: [none, imagenet]
  transform_config:
    train: null
    eval: null
  test_split_mode: from_dir # options: [from_dir, synthetic]
  test_split_ratio: 0.2 # fraction of train images held out testing (usage depends on test_split_mode)
  val_split_mode: same_as_test # options: [same_as_test, from_test, synthetic]
  val_split_ratio: 0.5 # fraction of train/test images held out for validation (usage depends on val_split_mode)
  tiling:
    apply: false
    tile_size: null
    stride: null
    remove_border_count: 0
    use_random_tiling: False
    random_tile_count: 16
```

