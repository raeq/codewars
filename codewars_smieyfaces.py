"""
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

"""


def count_smileys(arr):
    ret_value = 0

    valid = set()
    eyes = [':', ';']
    nose = ['', '-', '~']
    mouth = [')', 'D']

    for e in eyes:
        for n in nose:
            for m in mouth:
                valid.add(f"{e}{n}{m}")

    for face in arr:
        if face in valid:
            ret_value += 1

    return ret_value


assert (count_smileys([]) == 0)
assert (count_smileys([':D', ':~)', ';~D', ':)']) == 4)
assert (count_smileys([':)', ':(', ':D', ':O', ':;']) == 2)
assert (count_smileys([';]', ':[', ';*', ':$', ';-D']) == 1)
