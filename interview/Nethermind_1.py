def solution(letters: str) -> int:

    removed = set()
    valid_letters = set()
    occurrence = set()

    for s in letters:
    # If already removed - do nothing
        if not s.lower() in removed:

        # Check lower, two cases
        # 1. First occurrence, no upper - add to array
        # 2. Uppers exists, remove from valid letters and mark as removed
            if s.islower():

                if s.upper() in occurrence:
                    removed.add(s)
                    if s.lower() in valid_letters:
                        valid_letters.remove(s)
                else:
                   occurrence.add(s)

                # Check upper, two cases
                # 1. Lower exists - add to valid letters
                # 2. Just add to occurrence
            else:
                if s.lower() in occurrence:
                    valid_letters.add(s.lower())
                occurrence.add(s)

    return len(valid_letters)



if __name__ == '__main__':

    res = solution('aaaAAbbBCcc')
    assert res == 2

    res = solution('aaaAAabbBCcc')
    assert res == 1

    res = solution('')
    assert res == 0

    res = solution('ccccCCCCccaaa')
    assert res == 0

    res = solution('ccccCCCCccaaabbbbBBB')
    assert res == 1