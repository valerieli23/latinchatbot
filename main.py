from cltk.stem.latin.declension import CollatinusDecliner
#from cltk.tokenize.word import WordTokenizer
from cltk.stem.lemma import LemmaReplacer
from cltk.semantics.latin.lookup import Synonyms

decliner = CollatinusDecliner()
#word_tokenizer = WordTokenizer('latin')
lemmatizer = LemmaReplacer('latin')
translator = Synonyms(dictionary='synonyms', language = 'latin')

