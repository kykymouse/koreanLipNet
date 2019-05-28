# -*- coding: utf-8 -*- 
from keras import backend as K
import numpy as np

def _decode(y_pred, input_length, greedy=True, beam_width=100, top_paths=1):
    """Decodes the output of a softmax.
    Can use either greedy search (also known as best path)
    or a constrained dictionary search.
    # Arguments
        y_pred: tensor `(samples, time_steps, num_categories)`
            containing the prediction, or output of the softmax.
        input_length: tensor `(samples, )` containing the sequence length for
            each batch item in `y_pred`.
        greedy: perform much faster best-path search if `true`.
            This does not use a dictionary.
        beam_width: if `greedy` is `false`: a beam search decoder will be used
            with a beam of this width.
        top_paths: if `greedy` is `false`,
            how many of the most probable paths will be returned.
    # Returns
        Tuple:
            List: if `greedy` is `true`, returns a list of one element that
                contains the decoded sequence.
                If `false`, returns the `top_paths` most probableo
                decoded sequences.
                Important: blank labels are returned as `-1`.
            Tensor `(top_paths, )` that contains
                the log probability of each decoded sequence.
    """
    decoded = K.ctc_decode(y_pred=y_pred, input_length=input_length,
                           greedy=greedy, beam_width=beam_width, top_paths=top_paths)
    #print y_pred

    print "path.eval+++++"
    for path in decoded[0]:
        print path.eval(session=K.get_session())

    print "+++++path.eval"

    # print "&&&&&path&&&&&"
    paths = [path.eval(session=K.get_session()) for path in decoded[0]]
    # print "&&&&&"

    print "logprobs$$$$$$$$$$$$$"
    logprobs  = decoded[1].eval(session=K.get_session())
    print logprobs
    return (paths, logprobs)

def decode(y_pred, input_length, greedy=True, beam_width=100, top_paths=1, **kwargs):
    language_model = kwargs.get('language_model', None)

    print "@@@@@@@@@@@@@decode@@@@@@@@@@@@@"
    print y_pred
    print "######################"
    print input_length
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    paths, logprobs = _decode(y_pred=y_pred, input_length=input_length,
                              greedy=greedy, beam_width=beam_width, top_paths=top_paths)
    print "paths : " + str(paths)
    print "log : " + str(logprobs)

    if language_model is not None:
        # TODO: compute using language model
        raise NotImplementedError("Language model search is not implemented yet")
    else:
        # simply output highest probability sequence
        # paths has been sorted from the start
        result = paths[0]
    return result

class Decoder(object):
    def __init__(self, greedy=True, beam_width=100, top_paths=1, **kwargs):
        self.greedy         = greedy
        self.beam_width     = beam_width
        self.top_paths      = top_paths
        self.language_model = kwargs.get('language_model', None)
        self.postprocessors = kwargs.get('postprocessors', []) #labels_to_text, spell.sentence

    def decode(self, y_pred, input_length):
        decoded = decode(y_pred, input_length, greedy=self.greedy, beam_width=self.beam_width,
                         top_paths=self.top_paths, language_model=self.language_model)
        preprocessed = []

        for output in decoded: #decoded 한번 돔(아마 여기서 여러번 돌아야 여러 문장이 가능)            
            out = output

            for postprocessor in self.postprocessors: # 2번 실행 labels_to_text -> spell.sentence
                out = postprocessor(out)
            preprocessed.append(out)

        return preprocessed