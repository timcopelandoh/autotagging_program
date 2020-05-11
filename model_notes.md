handwriting_001 - 20 epochs, trained to test other programs
handwriting_002 - 300 epochs, dropout weights 0.15, 0.35. Trained to minimized val_loss, which occurred early. Model got more accurate throughout, even though loss increased. - best accuracy 71%, best loss 1.57
handwriting_003 - 250 epochs, same weights, set checkpoints to optimize on both loss and accuracy. - best accuracy 63%, best loss 1.91
handwriting_004 - 250 epochs, removed Adam and Ben (8 pictures each) - best accuracy 74%, best loss 1.16
handwriting_005 - 350 epochs, dropout weights 0.25, 0.5 - best accuracy 74%, best loss .90
handwriting_006 - 400 epochs, dropout weights 0.3, 0.6 - best accuracy 74%, best loss 1.15
handwriting_007 - 400 epoches, dropout weights 0.5, 0.5 - best accuracy 90%, best loss 0.43
handwriting_008 - 400 epoches, same as before, validating results - best accuracy 69%, best loss 1.21 (weird and I'm not sure what do with this)
