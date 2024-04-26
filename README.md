# Yolov3-Jetdetection
Trained YOLO model to detect jets

# Example images

![test_batch0](https://github.com/ibrahim737701/Yolov3-Jetdetection/assets/51760306/25fe86d0-b507-4ef9-8c95-1612cce28545)

![60](https://github.com/ibrahim737701/Yolov3-Jetdetection/assets/51760306/4931b843-a323-4085-aefe-0ce7340ae965)
![55](https://github.com/ibrahim737701/Yolov3-Jetdetection/assets/51760306/e1a0365f-4f8d-4c61-8075-601fb108c8b3)
![51](https://github.com/ibrahim737701/Yolov3-Jetdetection/assets/51760306/de7e930e-f0db-4b3a-86e0-5d80b8c2fcab)
![47](https://github.com/ibrahim737701/Yolov3-Jetdetection/assets/51760306/cf07b553-f143-4632-98fd-822e6743efa4)
![46](https://github.com/ibrahim737701/Yolov3-Jetdetection/assets/51760306/b9105428-aec0-4930-84d1-583f293ebc2e)
![39](https://github.com/ibrahim737701/Yolov3-Jetdetection/assets/51760306/56dfa74b-2331-48f7-811a-a3084db21f1b)
![11](https://github.com/ibrahim737701/Yolov3-Jetdetection/assets/51760306/ba6c3d4e-93e2-459c-9775-01d88958fda9)
![10](https://github.com/ibrahim737701/Yolov3-Jetdetection/assets/51760306/7e2cdff7-1fe0-4445-8035-27b1bffdf761)
![7](https://github.com/ibrahim737701/Yolov3-Jetdetection/assets/51760306/9996c357-f32d-4d63-81dc-5d48664172a3)
![3](https://github.com/ibrahim737701/Yolov3-Jetdetection/assets/51760306/919459ef-787d-4f2c-9d38-7cb3b3002df9)

# Training logs

       Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.19it/s]
                 all        97       168     0.895     0.601     0.711     0.719

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   135/299     8.25G      2.03     0.622         0      2.65        24       512: 100%|███████████████| 10/10 [00:01<00:00,  7.88it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.36it/s]
                 all        97       168     0.896     0.612     0.711     0.727

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   136/299     8.25G      1.98     0.461         0      2.44        18       512: 100%|███████████████| 10/10 [00:01<00:00,  7.64it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.72it/s]
                 all        97       168     0.927     0.601     0.705     0.729

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   137/299     8.25G      2.01     0.603         0      2.62        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.73it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.80it/s]
                 all        97       168     0.911     0.608     0.693     0.729

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   138/299     8.25G      2.16      0.58         0      2.74        20       512: 100%|███████████████| 10/10 [00:01<00:00,  7.81it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.57it/s]
                 all        97       168     0.875     0.637     0.703     0.737

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   139/299     8.25G      2.05     0.516         0      2.56        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.72it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.56it/s]
                 all        97       168     0.857     0.637     0.715     0.731

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   140/299     8.25G      1.95     0.585         0      2.53        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.83it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.36it/s]
                 all        97       168     0.951     0.649     0.742     0.771

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   141/299     8.25G      1.97     0.492         0      2.46        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.56it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.47it/s]
                 all        97       168     0.965     0.637     0.742     0.767

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   142/299     8.25G      1.79     0.563         0      2.35        20       512: 100%|███████████████| 10/10 [00:01<00:00,  7.70it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.05it/s]
                 all        97       168     0.977     0.583     0.729     0.731

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   143/299     8.25G      1.72      0.57         0      2.29        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.83it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.44it/s]
                 all        97       168     0.971     0.605     0.713     0.745

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   144/299     8.25G      1.71     0.482         0      2.19        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.86it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.47it/s]
                 all        97       168     0.925     0.588     0.696     0.719

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   145/299     8.25G      1.85     0.528         0      2.38        10       512: 100%|███████████████| 10/10 [00:01<00:00,  7.91it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.30it/s]
                 all        97       168     0.917     0.589     0.704     0.717

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   146/299     8.25G      1.83     0.594         0      2.42        22       512: 100%|███████████████| 10/10 [00:01<00:00,  7.79it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.44it/s]
                 all        97       168     0.972     0.614     0.733     0.753

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   147/299     8.25G      2.21     0.476         0      2.68        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.81it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.41it/s]
                 all        97       168     0.981     0.605     0.743     0.748

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   148/299     8.25G      1.66     0.553         0      2.21        10       512: 100%|███████████████| 10/10 [00:01<00:00,  7.83it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.61it/s]
                 all        97       168     0.972     0.619     0.758     0.757

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   149/299     8.25G      1.51     0.613         0      2.13        20       512: 100%|███████████████| 10/10 [00:01<00:00,  7.89it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.54it/s]
                 all        97       168     0.963     0.621     0.754     0.755

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   150/299     8.25G      1.74     0.593         0      2.33        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.72it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.28it/s]
                 all        97       168      0.98     0.589     0.762     0.736

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   151/299     8.25G      1.58     0.514         0       2.1        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.64it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.43it/s]
                 all        97       168      0.99     0.597     0.769     0.745

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   152/299     8.25G      1.96     0.568         0      2.53        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.91it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.30it/s]
                 all        97       168     0.972     0.625     0.749     0.761

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   153/299     8.25G      1.55     0.543         0       2.1        12       512: 100%|███████████████| 10/10 [00:01<00:00,  7.74it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.42it/s]
                 all        97       168     0.982     0.639     0.752     0.774

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   154/299     8.25G      1.75     0.501         0      2.25        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.51it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.78it/s]
                 all        97       168     0.964     0.643     0.741     0.771

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   155/299     8.25G       1.9     0.574         0      2.47        25       512: 100%|███████████████| 10/10 [00:01<00:00,  7.90it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.42it/s]
                 all        97       168      0.96     0.637     0.746     0.766

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   156/299     8.25G      1.73     0.531         0      2.26        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.95it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.50it/s]
                 all        97       168     0.972      0.62     0.751     0.757

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   157/299     8.25G       2.3     0.536         0      2.84        15       512: 100%|███████████████| 10/10 [00:01<00:00,  8.01it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.39it/s]
                 all        97       168     0.972     0.625     0.727     0.761

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   158/299     8.25G      1.67     0.603         0      2.28        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.79it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.55it/s]
                 all        97       168      0.97     0.631     0.736     0.765

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   159/299     8.25G      1.76     0.551         0      2.31        12       512: 100%|███████████████| 10/10 [00:01<00:00,  7.84it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.63it/s]
                 all        97       168     0.965     0.655     0.741     0.781

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   160/299     8.25G      1.86     0.515         0      2.37        25       512: 100%|███████████████| 10/10 [00:01<00:00,  7.81it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.67it/s]
                 all        97       168     0.974     0.658     0.759     0.785

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   161/299     8.25G       1.6     0.495         0       2.1        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.87it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.19it/s]
                 all        97       168     0.973      0.65     0.753     0.779

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   162/299     8.25G      1.47     0.566         0      2.04        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.74it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.43it/s]
                 all        97       168     0.981     0.623     0.745     0.762

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   163/299     8.25G      1.84     0.564         0       2.4        19       512: 100%|███████████████| 10/10 [00:01<00:00,  7.63it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.48it/s]
                 all        97       168     0.981     0.624     0.733     0.763

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   164/299     8.25G      1.76     0.564         0      2.33        25       512: 100%|███████████████| 10/10 [00:01<00:00,  7.73it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.62it/s]
                 all        97       168     0.964     0.635     0.716     0.766

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   165/299     8.25G      1.72     0.535         0      2.25        11       512: 100%|███████████████| 10/10 [00:01<00:00,  7.86it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.40it/s]
                 all        97       168     0.955     0.639     0.714     0.766

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   166/299     8.25G      1.59     0.613         0       2.2        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.84it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.66it/s]
                 all        97       168     0.939     0.636     0.711     0.758

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   167/299     8.25G      1.78     0.477         0      2.26        18       512: 100%|███████████████| 10/10 [00:01<00:00,  7.84it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.44it/s]
                 all        97       168     0.948     0.653     0.722     0.773

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   168/299     8.25G      1.53     0.549         0      2.08        23       512: 100%|███████████████| 10/10 [00:01<00:00,  7.74it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.39it/s]
                 all        97       168     0.944     0.643      0.74     0.765

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   169/299     8.25G      1.59     0.571         0      2.16        20       512: 100%|███████████████| 10/10 [00:01<00:00,  7.86it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.38it/s]
                 all        97       168     0.945     0.655     0.737     0.774

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   170/299     8.25G      1.67      0.56         0      2.23        15       512: 100%|███████████████| 10/10 [00:01<00:00,  7.72it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.50it/s]
                 all        97       168     0.948     0.652     0.734     0.773

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   171/299     8.25G       1.6     0.508         0       2.1        12       512: 100%|███████████████| 10/10 [00:01<00:00,  7.77it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.29it/s]
                 all        97       168     0.947     0.633     0.733     0.759

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   172/299     8.25G      1.73     0.544         0      2.28        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.76it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.49it/s]
                 all        97       168     0.947     0.642     0.717     0.765

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   173/299     8.25G      1.42     0.549         0      1.97        19       512: 100%|███████████████| 10/10 [00:01<00:00,  7.87it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.53it/s]
                 all        97       168     0.931     0.645     0.709     0.762

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   174/299     8.25G      1.59     0.472         0      2.06        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.74it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.49it/s]
                 all        97       168      0.94     0.649      0.72     0.767

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   175/299     8.25G      1.24     0.479         0      1.72        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.85it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.51it/s]
                 all        97       168     0.915     0.643     0.701     0.756

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   176/299     8.25G      1.56     0.521         0      2.08        15       512: 100%|███████████████| 10/10 [00:01<00:00,  7.84it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.55it/s]
                 all        97       168     0.931     0.644     0.739     0.762

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   177/299     8.25G      1.56     0.582         0      2.15        21       512: 100%|███████████████| 10/10 [00:01<00:00,  7.80it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.60it/s]
                 all        97       168     0.957     0.669     0.758     0.788

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   178/299     8.25G       1.6     0.509         0      2.11        12       512: 100%|███████████████| 10/10 [00:01<00:00,  7.72it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.54it/s]
                 all        97       168     0.954     0.667     0.768     0.785

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   179/299     8.25G       1.7     0.456         0      2.16        10       512: 100%|███████████████| 10/10 [00:01<00:00,  7.82it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.63it/s]
                 all        97       168     0.949     0.667     0.765     0.784

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   180/299     8.25G      1.83     0.475         0      2.31        18       512: 100%|███████████████| 10/10 [00:01<00:00,  7.60it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.48it/s]
                 all        97       168     0.949     0.661     0.764     0.779

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   181/299     8.25G      1.37     0.514         0      1.88        24       512: 100%|███████████████| 10/10 [00:01<00:00,  7.90it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.55it/s]
                 all        97       168     0.948     0.657     0.762     0.776

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   182/299     8.25G      1.51     0.489         0         2        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.67it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.48it/s]
                 all        97       168     0.949     0.659     0.766     0.778

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   183/299     8.25G      1.66     0.471         0      2.13        14       512: 100%|███████████████| 10/10 [00:01<00:00,  8.04it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.40it/s]
                 all        97       168     0.949     0.666     0.767     0.783

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   184/299     8.25G      1.63     0.447         0      2.08        10       512: 100%|███████████████| 10/10 [00:01<00:00,  7.92it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.46it/s]
                 all        97       168     0.942     0.671     0.766     0.784

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   185/299     8.25G      1.26     0.485         0      1.75        23       512: 100%|███████████████| 10/10 [00:01<00:00,  7.86it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.17it/s]
                 all        97       168     0.943     0.667     0.753     0.781

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   186/299     8.25G      1.44     0.429         0      1.87        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.90it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.69it/s]
                 all        97       168      0.95     0.683     0.757     0.795

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   187/299     8.25G      1.67     0.508         0      2.18        19       512: 100%|███████████████| 10/10 [00:01<00:00,  7.95it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.50it/s]
                 all        97       168     0.942      0.69     0.758     0.797

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   188/299     8.25G      1.69     0.502         0      2.19        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.93it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.23it/s]
                 all        97       168     0.942     0.672     0.766     0.784

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   189/299     8.25G      1.45     0.527         0      1.98        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.85it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.30it/s]
                 all        97       168      0.94     0.654      0.75     0.772

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   190/299     8.25G      1.48     0.517         0         2        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.69it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.59it/s]
                 all        97       168     0.949     0.665      0.73     0.782

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   191/299     8.25G       1.3     0.508         0      1.81        18       512: 100%|███████████████| 10/10 [00:01<00:00,  7.73it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.60it/s]
                 all        97       168     0.934     0.679     0.746     0.787

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   192/299     8.25G      1.74     0.441         0      2.18        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.90it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.33it/s]
                 all        97       168     0.942      0.69     0.752     0.797

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   193/299     8.25G      1.54     0.522         0      2.07        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.84it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.32it/s]
                 all        97       168     0.942      0.69     0.765     0.797

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   194/299     8.25G      1.71     0.472         0      2.19        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.73it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.56it/s]
                 all        97       168     0.955      0.69     0.789     0.802

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   195/299     8.25G      1.44     0.509         0      1.95        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.69it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.68it/s]
                 all        97       168     0.951     0.689     0.778     0.799

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   196/299     8.25G      1.27      0.43         0       1.7        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.87it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.47it/s]
                 all        97       168     0.961     0.679     0.759     0.795

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   197/299     8.25G      1.62     0.525         0      2.15        21       512: 100%|███████████████| 10/10 [00:01<00:00,  7.71it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.79it/s]
                 all        97       168     0.951     0.696      0.76     0.804

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   198/299     8.25G      1.52     0.518         0      2.04        24       512: 100%|███████████████| 10/10 [00:01<00:00,  7.61it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.49it/s]
                 all        97       168     0.935     0.696      0.76     0.798

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   199/299     8.25G       1.6     0.477         0      2.08        22       512: 100%|███████████████| 10/10 [00:01<00:00,  7.68it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.55it/s]
                 all        97       168     0.943     0.695     0.763     0.801

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   200/299     8.25G      1.47     0.472         0      1.95        20       512: 100%|███████████████| 10/10 [00:01<00:00,  7.83it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.38it/s]
                 all        97       168     0.952      0.69     0.775       0.8

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   201/299     8.25G      1.28     0.405         0      1.69        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.86it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.44it/s]
                 all        97       168     0.963     0.673     0.746     0.792

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   202/299     8.25G      1.57     0.492         0      2.06        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.72it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.58it/s]
                 all        97       168     0.961     0.661      0.74     0.783

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   203/299     8.25G      1.34     0.395         0      1.74        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.81it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.46it/s]
                 all        97       168     0.956     0.643     0.752     0.769

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   204/299     8.25G      1.53      0.48         0      2.01        19       512: 100%|███████████████| 10/10 [00:01<00:00,  7.69it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.56it/s]
                 all        97       168     0.956     0.652     0.745     0.775

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   205/299     8.25G      1.32     0.424         0      1.75        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.69it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.41it/s]
                 all        97       168     0.957     0.664      0.75     0.784

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   206/299     8.25G      1.32     0.435         0      1.75        12       512: 100%|███████████████| 10/10 [00:01<00:00,  7.83it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.41it/s]
                 all        97       168     0.949     0.671     0.761     0.786

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   207/299     8.25G      1.28     0.378         0      1.66        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.69it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.46it/s]
                 all        97       168     0.949     0.669     0.766     0.785

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   208/299     8.25G      1.26     0.427         0      1.68        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.72it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.44it/s]
                 all        97       168     0.958     0.682     0.783     0.797

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   209/299     8.25G       1.4     0.478         0      1.88        21       512: 100%|███████████████| 10/10 [00:01<00:00,  7.87it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.55it/s]
                 all        97       168     0.955     0.679     0.781     0.793

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   210/299     8.25G       1.8     0.462         0      2.27        12       512: 100%|███████████████| 10/10 [00:01<00:00,  7.74it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.50it/s]
                 all        97       168     0.942     0.673     0.778     0.785

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   211/299     8.25G      1.59     0.498         0      2.08        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.72it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.16it/s]
                 all        97       168     0.956     0.673     0.775      0.79

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   212/299     8.25G      1.44     0.425         0      1.86        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.64it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.03it/s]
                 all        97       168     0.949     0.649     0.757     0.771

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   213/299     8.25G      1.25      0.38         0      1.63        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.87it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.60it/s]
                 all        97       168     0.943     0.649     0.745     0.769

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   214/299     8.25G      1.57     0.464         0      2.03        18       512: 100%|███████████████| 10/10 [00:01<00:00,  7.79it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.61it/s]
                 all        97       168     0.937     0.613     0.716     0.741

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   215/299     8.25G      1.57     0.421         0      1.99        19       512: 100%|███████████████| 10/10 [00:01<00:00,  7.90it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.64it/s]
                 all        97       168     0.955     0.589     0.701     0.729

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   216/299     8.25G      1.33     0.475         0      1.81        20       512: 100%|███████████████| 10/10 [00:01<00:00,  7.78it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.60it/s]
                 all        97       168     0.934     0.595     0.699     0.727

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   217/299     8.25G      1.43     0.412         0      1.84        11       512: 100%|███████████████| 10/10 [00:01<00:00,  7.85it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.67it/s]
                 all        97       168     0.934     0.592     0.702     0.724

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   218/299     8.25G      1.52     0.466         0      1.98        19       512: 100%|███████████████| 10/10 [00:01<00:00,  7.71it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.65it/s]
                 all        97       168     0.935     0.602     0.693     0.733

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   219/299     8.25G      1.54     0.415         0      1.95        17       512: 100%|███████████████| 10/10 [00:01<00:00,  8.01it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.63it/s]
                 all        97       168     0.945     0.607      0.69     0.739

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   220/299     8.25G      1.44     0.382         0      1.82        23       512: 100%|███████████████| 10/10 [00:01<00:00,  7.70it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.54it/s]
                 all        97       168     0.946     0.622      0.72      0.75

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   221/299     8.25G       1.5     0.431         0      1.93        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.73it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.51it/s]
                 all        97       168     0.955     0.636     0.732     0.764

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   222/299     8.25G      1.31     0.501         0      1.81        21       512: 100%|███████████████| 10/10 [00:01<00:00,  7.63it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.66it/s]
                 all        97       168     0.951     0.643     0.742     0.767

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   223/299     8.25G      1.38      0.49         0      1.87        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.80it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.36it/s]
                 all        97       168     0.946      0.63      0.73     0.757

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   224/299     8.25G      1.58     0.418         0         2        15       512: 100%|███████████████| 10/10 [00:01<00:00,  7.64it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.51it/s]
                 all        97       168     0.947     0.643     0.726     0.766

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   225/299     8.25G      1.14      0.41         0      1.55        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.86it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.44it/s]
                 all        97       168     0.935     0.643     0.724     0.762

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   226/299     8.25G      1.36     0.346         0       1.7        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.76it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.54it/s]
                 all        97       168     0.928     0.643     0.713      0.76

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   227/299     8.25G      1.35     0.464         0      1.82        24       512: 100%|███████████████| 10/10 [00:01<00:00,  7.89it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.37it/s]
                 all        97       168     0.953     0.655     0.729     0.776

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   228/299     8.25G       1.4     0.422         0      1.82        21       512: 100%|███████████████| 10/10 [00:01<00:00,  7.85it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.50it/s]
                 all        97       168     0.957     0.661     0.733     0.782

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   229/299     8.25G      1.53     0.429         0      1.96        19       512: 100%|███████████████| 10/10 [00:01<00:00,  7.77it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.69it/s]
                 all        97       168     0.957     0.667     0.741     0.786

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   230/299     8.25G      1.33     0.487         0      1.82        19       512: 100%|███████████████| 10/10 [00:01<00:00,  7.82it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.47it/s]
                 all        97       168     0.949     0.666     0.746     0.783

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   231/299     8.25G      1.53     0.411         0      1.94        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.99it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.10it/s]
                 all        97       168     0.951     0.661     0.747      0.78

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   232/299     8.25G      1.23     0.432         0      1.66        15       512: 100%|███████████████| 10/10 [00:01<00:00,  6.94it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.55it/s]
                 all        97       168     0.949      0.66     0.734     0.778

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   233/299     8.25G      1.56     0.441         0         2        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.71it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.36it/s]
                 all        97       168      0.95     0.661     0.742     0.779

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   234/299     8.25G      1.27     0.435         0       1.7        22       512: 100%|███████████████| 10/10 [00:01<00:00,  7.92it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.28it/s]
                 all        97       168      0.94     0.655     0.738     0.772

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   235/299     8.25G      1.37      0.44         0      1.81        12       512: 100%|███████████████| 10/10 [00:01<00:00,  7.97it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.65it/s]
                 all        97       168     0.951     0.661     0.744      0.78

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   236/299     8.25G      1.11     0.397         0      1.51        20       512: 100%|███████████████| 10/10 [00:01<00:00,  7.88it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.44it/s]
                 all        97       168     0.948     0.655     0.748     0.775

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   237/299     8.25G      1.04     0.464         0      1.51        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.88it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.63it/s]
                 all        97       168     0.949     0.649     0.733     0.771

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   238/299     8.25G      1.22     0.425         0      1.64        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.81it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.42it/s]
                 all        97       168     0.945     0.649     0.726     0.769

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   239/299     8.25G      1.16     0.405         0      1.56        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.87it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.56it/s]
                 all        97       168     0.946     0.649     0.722      0.77

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   240/299     8.25G       1.3     0.472         0      1.78        22       512: 100%|███████████████| 10/10 [00:01<00:00,  7.80it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.55it/s]
                 all        97       168     0.949     0.637     0.722     0.762

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   241/299     8.25G       1.3     0.442         0      1.74        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.88it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.33it/s]
                 all        97       168     0.939     0.631     0.727     0.755

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   242/299     8.25G      1.24     0.357         0       1.6        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.63it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.48it/s]
                 all        97       168     0.931     0.637     0.728     0.756

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   243/299     8.25G      1.23     0.429         0      1.66        21       512: 100%|███████████████| 10/10 [00:01<00:00,  7.68it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.66it/s]
                 all        97       168     0.931     0.641     0.727     0.759

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   244/299     8.25G      1.18     0.403         0      1.58        18       512: 100%|███████████████| 10/10 [00:01<00:00,  7.81it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.59it/s]
                 all        97       168     0.931     0.639     0.727     0.758

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   245/299     8.25G      1.41     0.428         0      1.84        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.73it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.33it/s]
                 all        97       168     0.945     0.649     0.743     0.769

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   246/299     8.25G      1.37     0.379         0      1.74        12       512: 100%|███████████████| 10/10 [00:01<00:00,  7.75it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.33it/s]
                 all        97       168     0.948     0.643     0.735     0.766

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   247/299     8.25G      1.19     0.382         0      1.57        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.80it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.26it/s]
                 all        97       168     0.942     0.649     0.745     0.768

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   248/299     8.25G     0.994     0.349         0      1.34        12       512: 100%|███████████████| 10/10 [00:01<00:00,  7.85it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.38it/s]
                 all        97       168     0.941     0.659     0.744     0.775

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   249/299     8.25G      1.33     0.386         0      1.72        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.82it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.52it/s]
                 all        97       168      0.94     0.657     0.736     0.774

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   250/299     8.25G      1.27      0.41         0      1.68        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.88it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.60it/s]
                 all        97       168     0.945     0.643     0.735     0.765

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   251/299     8.25G      1.11     0.367         0      1.48        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.87it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.62it/s]
                 all        97       168     0.956     0.641     0.739     0.767

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   252/299     8.25G       1.2     0.389         0      1.59        23       512: 100%|███████████████| 10/10 [00:01<00:00,  7.73it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.35it/s]
                 all        97       168     0.956     0.649     0.738     0.773

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   253/299     8.25G      1.29     0.395         0      1.68        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.78it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.56it/s]
                 all        97       168     0.956     0.653     0.736     0.776

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   254/299     8.25G      1.17     0.376         0      1.55        12       512: 100%|███████████████| 10/10 [00:01<00:00,  7.79it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.43it/s]
                 all        97       168     0.957     0.656     0.734     0.778

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   255/299     8.25G      1.32     0.425         0      1.75        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.70it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.27it/s]
                 all        97       168     0.948     0.661     0.735     0.779

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   256/299     8.25G      1.12     0.369         0      1.49        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.78it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.29it/s]
                 all        97       168     0.946     0.661     0.737     0.778

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   257/299     8.25G      1.19     0.415         0      1.61        25       512: 100%|███████████████| 10/10 [00:01<00:00,  7.90it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.53it/s]
                 all        97       168     0.946     0.661     0.732     0.778

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   258/299     8.25G      1.43     0.394         0      1.82        19       512: 100%|███████████████| 10/10 [00:01<00:00,  7.83it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.39it/s]
                 all        97       168     0.949     0.662      0.74      0.78

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   259/299     8.25G     0.953     0.373         0      1.33         9       512: 100%|███████████████| 10/10 [00:01<00:00,  7.83it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.70it/s]
                 all        97       168     0.949      0.66      0.74     0.778

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   260/299     8.25G      1.19     0.417         0       1.6        22       512: 100%|███████████████| 10/10 [00:01<00:00,  7.75it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.52it/s]
                 all        97       168     0.949      0.66     0.743     0.778

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   261/299     8.25G      1.23     0.382         0      1.61        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.72it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.34it/s]
                 all        97       168     0.949     0.659     0.737     0.778

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   262/299     8.25G      1.41     0.385         0       1.8        19       512: 100%|███████████████| 10/10 [00:01<00:00,  7.72it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.48it/s]
                 all        97       168     0.939     0.661     0.736     0.776

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   263/299     8.25G      1.17     0.377         0      1.55        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.87it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.29it/s]
                 all        97       168     0.938     0.661     0.734     0.775

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   264/299     8.25G      1.18     0.382         0      1.56        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.84it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.58it/s]
                 all        97       168     0.938     0.661     0.732     0.775

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   265/299     8.25G      1.19     0.396         0      1.58        18       512: 100%|███████████████| 10/10 [00:01<00:00,  7.80it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.34it/s]
                 all        97       168     0.941     0.659     0.726     0.775

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   266/299     8.25G      1.33     0.358         0      1.69        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.85it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.48it/s]
                 all        97       168     0.945     0.655     0.733     0.773

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   267/299     8.25G      1.22     0.376         0      1.59        23       512: 100%|███████████████| 10/10 [00:01<00:00,  8.00it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.44it/s]
                 all        97       168     0.947     0.655     0.732     0.774

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   268/299     8.25G      1.24     0.351         0       1.6        12       512: 100%|███████████████| 10/10 [00:01<00:00,  7.86it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.88it/s]
                 all        97       168     0.948     0.652      0.73     0.772

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   269/299     8.25G      1.15     0.431         0      1.58        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.94it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.47it/s]
                 all        97       168     0.943     0.649     0.724     0.769

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   270/299     8.25G      1.43     0.408         0      1.84        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.85it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.47it/s]
                 all        97       168     0.936     0.649     0.746     0.767

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   271/299     8.25G     0.938     0.393         0      1.33        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.83it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.50it/s]
                 all        97       168     0.932     0.654     0.747     0.769

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   272/299     8.25G      1.08     0.314         0       1.4        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.85it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.31it/s]
                 all        97       168     0.933     0.658     0.741     0.772

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   273/299     8.25G      1.11     0.413         0      1.53        21       512: 100%|███████████████| 10/10 [00:01<00:00,  7.63it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.38it/s]
                 all        97       168     0.941     0.661      0.74     0.776

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   274/299     8.25G      1.23     0.366         0       1.6        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.77it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.19it/s]
                 all        97       168     0.949      0.66     0.738     0.779

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   275/299     8.25G      1.17     0.387         0      1.56        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.86it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.73it/s]
                 all        97       168     0.949     0.664     0.737     0.781

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   276/299     8.25G      1.12     0.341         0      1.46        11       512: 100%|███████████████| 10/10 [00:01<00:00,  7.80it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.53it/s]
                 all        97       168     0.954     0.661     0.734     0.781

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   277/299     8.25G      1.06     0.333         0      1.39        14       512: 100%|███████████████| 10/10 [00:01<00:00,  7.85it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.31it/s]
                 all        97       168     0.956     0.661     0.734     0.781

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   278/299     8.25G       1.3     0.361         0      1.66        20       512: 100%|███████████████| 10/10 [00:01<00:00,  7.90it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.50it/s]
                 all        97       168     0.954     0.661     0.734     0.781

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   279/299     8.25G      1.41     0.392         0       1.8        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.81it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.01it/s]
                 all        97       168     0.957      0.66     0.735     0.781

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   280/299     8.25G      1.15     0.402         0      1.56        12       512: 100%|███████████████| 10/10 [00:01<00:00,  7.63it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.55it/s]
                 all        97       168     0.957     0.655     0.735     0.777

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   281/299     8.25G      1.28     0.345         0      1.62        18       512: 100%|███████████████| 10/10 [00:01<00:00,  7.81it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.46it/s]
                 all        97       168     0.957     0.659     0.736     0.781

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   282/299     8.25G      1.18     0.364         0      1.54        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.87it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.52it/s]
                 all        97       168     0.957     0.662     0.738     0.783

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   283/299     8.25G      1.19      0.36         0      1.55        21       512: 100%|███████████████| 10/10 [00:01<00:00,  7.95it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.52it/s]
                 all        97       168     0.957      0.67     0.739     0.789

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   284/299     8.25G      1.13     0.369         0       1.5        22       512: 100%|███████████████| 10/10 [00:01<00:00,  7.67it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.35it/s]
                 all        97       168     0.957     0.673      0.74      0.79

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   285/299     8.25G      1.19     0.365         0      1.56        17       512: 100%|███████████████| 10/10 [00:01<00:00,  7.86it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.34it/s]
                 all        97       168     0.958     0.673      0.74     0.791

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   286/299     8.25G      1.37     0.393         0      1.76        20       512: 100%|███████████████| 10/10 [00:01<00:00,  7.83it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.34it/s]
                 all        97       168     0.957     0.669     0.741     0.788

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   287/299     8.25G       1.2     0.412         0      1.62        29       512: 100%|███████████████| 10/10 [00:01<00:00,  7.71it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.57it/s]
                 all        97       168     0.957     0.666     0.741     0.786

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   288/299     8.25G      1.23     0.349         0      1.58        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.66it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.61it/s]
                 all        97       168     0.957     0.673     0.741      0.79

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   289/299     8.25G      1.18      0.34         0      1.52        20       512: 100%|███████████████| 10/10 [00:01<00:00,  7.74it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.70it/s]
                 all        97       168     0.958     0.672     0.741      0.79

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   290/299     8.25G      1.22      0.36         0      1.58        15       512: 100%|███████████████| 10/10 [00:01<00:00,  7.84it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.65it/s]
                 all        97       168     0.958     0.678     0.743     0.794

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   291/299     8.25G     0.992     0.343         0      1.33        16       512: 100%|███████████████| 10/10 [00:01<00:00,  7.92it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.48it/s]
                 all        97       168     0.958      0.68     0.743     0.795

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   292/299     8.25G     0.989     0.308         0       1.3        15       512: 100%|███████████████| 10/10 [00:01<00:00,  7.63it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.74it/s]
                 all        97       168     0.958     0.681     0.742     0.796

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   293/299     8.25G      1.29     0.385         0      1.67        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.79it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.74it/s]
                 all        97       168     0.958     0.676     0.741     0.792

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   294/299     8.25G      1.14      0.32         0      1.46        18       512: 100%|███████████████| 10/10 [00:01<00:00,  7.78it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.52it/s]
                 all        97       168     0.958     0.674      0.74     0.791

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   295/299     8.25G      1.51     0.326         0      1.84        15       512: 100%|███████████████| 10/10 [00:01<00:00,  7.76it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.73it/s]
                 all        97       168     0.957      0.67     0.739     0.788

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   296/299     8.25G      1.31     0.452         0      1.76        24       512: 100%|███████████████| 10/10 [00:01<00:00,  7.76it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.39it/s]
                 all        97       168     0.957     0.665     0.738     0.785

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   297/299     8.25G      1.12     0.354         0      1.47        13       512: 100%|███████████████| 10/10 [00:01<00:00,  7.96it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.72it/s]
                 all        97       168     0.957     0.663     0.736     0.783

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   298/299     8.25G      1.16     0.389         0      1.55        19       512: 100%|███████████████| 10/10 [00:01<00:00,  7.78it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.30it/s]
                 all        97       168     0.957     0.665     0.735     0.785

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
   299/299     8.25G     0.911     0.299         0      1.21        11       512: 100%|███████████████| 10/10 [00:01<00:00,  7.71it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100%|███████████████| 10/10 [00:01<00:00,  8.57it/s]
                 all        97       168     0.957     0.665     0.736     0.785
300 epochs completed in 0.250 hours.
