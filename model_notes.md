simplecnn_001 - 20 epochs, trained to test other programs
simplecnn_002 - 300 epochs, dropout weights 0.15, 0.35. Trained to minimized val_loss, which occurred early. Model got more accurate throughout, even though loss increased. - best accuracy 71%, best loss 1.57
simplecnn_003 - 250 epochs, same weights, set checkpoints to optimize on both loss and accuracy. - best accuracy 63%, best loss 1.91
simplecnn_004 - 250 epochs, removed Adam and Ben (8 pictures each) - best accuracy 74%, best loss 1.16
simplecnn_005 - 350 epochs, dropout weights 0.25, 0.5 - best accuracy 74%, best loss .90
simplecnn_006 - 400 epochs, dropout weights 0.3, 0.6 - best accuracy 74%, best loss 1.15
simplecnn_007 - 400 epoches, dropout weights 0.5, 0.5 - best accuracy 90%, best loss 0.43
simplecnn_008 - 400 epoches, same as before, validating results - best accuracy 69%, best loss 1.21 (weird and I'm not sure what do with this)


levi-hassner_001 - 300 epochs, contains adam and ben again, dropout weights 0.25, 0.25 - best accuracy 80%, best loss .89
levi-hassner_002 - 300 epochs, same weights, softmax activation function - best accuracy 90%, best loss .66
levi-hassner_003 - 200 epochs, dropout weights 0.4, 0.4 - best accuracy 78%, best loss .95

note: not sure what happened to levi-hassner_003. It's possible it was fit under the name levi-hassner_002, and that got overwritten

levi-hassner_004 - 225 epochs, dropout weights 0.2, 0.2 - best accuracy 90%, best loss .58 - best loss weights also resulted in 88% accuracy. For what it's worth, these models performed very poorly out of the testing sample. Models were saved at epoch 193 and 172, so it's possible they were fairly overfit, and just happed to be able to do well on the testing dataset.
levi-hassner_005 - 300 epochs, dropout weights 0.3, 0.3 - best accuracy 76%, best loss 1.14
levi-hassner_006 - 150 epochs, dropout weights 0.5, 0.5 - best accuracy 90%, best loss .69
levi-hassner_007 - 150 epochs, dropout weights 0.55, 0.55 - best accuracy 88%, best loss .72
levi-hassner_008 - dropout weights 0.5, 0.5, trying stopping early, as soon as train and test accuracy diverge. Validation loss and accuracy consistently tracked above training, which was weird. Seems possible there was an easy test set. Good stats but didn't do well outside the test set. Saved after 80-90 epochs, stopped after 104 - best accuracy 90%, best loss 0.43