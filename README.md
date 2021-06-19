# siamese_sign
Model built using siamese architecture to analyze similarity in images

## Installation
```
pip install siamese-sign==0.1
```

## Usage
```
import tensorflow as tf
from siamese_sign import siamese_sign_verifier

r1, r2 = siamese_sign_verifier.get_images(image_path_1,
                                          image_path_2,
                                          128)

preds = siamese_sign_verifier.get_predictions(r1, r2)

0 - denotes the images match.
1 - denotes the images don't match.
```
