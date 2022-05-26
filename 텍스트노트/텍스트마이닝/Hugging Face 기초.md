# Hugging Face
- 허깅페이스는 트랜스포머를 기반으로 하는 다양한 모델(transformer.models)과 학습 스크립트(transformer.Trainer)를 구현해 놓은 모듈이다.
- 원래는 파이토치로 layer, model 등을 선언해주고 학습 스크립트도 전부 구현해야 하지만, 허깅 페이스를 사용하면 이런 수고를 덜 수 있다.
- 정리하면 '허깅 페이스'라는 회사가 만든 'transformers' 패키지가 있고, 일반적인 파이토치 구현체의 layer.py, model.py이 transformer.models에, train.py 가 transformer.Trainer에 대응된다.

