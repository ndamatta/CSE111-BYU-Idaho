from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    # 1. Test the single nouns.

    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from getnoun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns


def test_get_verb():
    # 1. Test the past verbs.

    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a single verb.
        word = get_verb(0, "past")

        # Verify that the word returned from get_verb
        # is one of the words in the past_verbs list.
        assert word in past_verbs

    # 2. Test the present verb WITH quantity 1.

    present_verb_quantity1 = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb which
        # should return a present verb with quantity 1.
        word = get_verb(1, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_verb_quantity1 list.
        assert word in present_verb_quantity1

    # 3. Test the present verb WITH NO quantity 1.

    present_verbs_no_quantity1 = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a present verb with no quantity 1.
        word = get_verb(3, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_verbs_no_quantity1 list.
        assert word in present_verbs_no_quantity1

    # 4. Test the future verb.

    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a future verb.
        word = get_verb(1, "future")

        # Verify that the word returned from get_verb
        # is one of the words in the future_verbs list.
        assert word in future_verbs
    

def test_get_noun():
    # 1. Test the single nouns.

    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from getnoun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns

def test_get_preposition():       
    # 1. Test prepositions
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_preposition function which
        # should return a random preposition.
        word = get_preposition()

        # Verify that the word returned from get_preposition
        # is one of the words in the plural_nouns list.
        assert word in prepositions

def test_get_prepositional_phrase():
    # 1. Test the single prepositional phrase.
    #Declare lists to test single prepositional phrase. Prepositions list works for both tests
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    single_determiners = ["a", "one", "the"]
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the single_prepositional_phrase function which
        # should return a single prepositional phrase. Then, split that phrase in a list.
        single_prepositional_phrase = get_prepositional_phrase(1)
        single_splitted_phrase = single_prepositional_phrase.split(" ")
        
        #Verify if prepositional phrase is made of 3 words
        assert len(single_splitted_phrase) == 3

        # Verify that the words stored in single_splitted_phrase are in its corresponding list
        assert single_splitted_phrase[0] in prepositions
        assert single_splitted_phrase[1] in single_determiners
        assert single_splitted_phrase[2] in single_nouns

    # 2. Test the plural prepositional phrase.
    #Declare lists to test plural prepositional phrase. Prepositions list works for both tests
    plural_determiners = ["some", "many", "the"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the plural_prepositional_phrase function which
        # should return a plural prepositional phrase. Then, split that phrase in a list.
        plural_prepositional_phrase = get_prepositional_phrase(2)
        plural_splitted_phrase = plural_prepositional_phrase.split(" ")
        
        #Verify if prepositional phrase is made of 3 words
        assert len(plural_splitted_phrase) == 3

        # Verify that the words stored in plural_splitted_phrase are in its corresponding list
        assert plural_splitted_phrase[0] in prepositions
        assert plural_splitted_phrase[1] in plural_determiners
        assert plural_splitted_phrase[2] in plural_nouns
    

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

# prepositional_phrase = get_prepositional_phrase(1)
# splitted_phrase = prepositional_phrase.split(" ")
# print(splitted_phrase)