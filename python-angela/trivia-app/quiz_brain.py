from html import unescape

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        """
        HTML escape characters are special codes used to display reserved characters like <, >, &, ", and ' correctly 
        in a web browser instead of being interpreted as HTML tags or attributes. 

        The most common escape sequences include:
        
        1. &lt; for the less-than sign (<)
        2. &gt; for the greater-than sign (>)
        3. &amp; for the ampersand (&)
        4. &quot; for double quotes (")
        5. &#39; or &apos; for single quotes (') 
        
        These characters are essential for preventing Cross-Site Scripting (XSS) attacks and ensuring text containing 
        HTML syntax is displayed as plain text. 
        
        Common Methods for Escaping HTML
        Different programming languages and tools provide specific functions to handle these conversions automatically:
        1. PHP: The htmlspecialchars() function converts special characters to HTML entities, with options like ENT_QUOTES 
        to handle both single and double quotes. 
        2. JavaScript: Developers often use String.prototype.replace() with regular expressions or create custom functions 
        to swap characters like &, <, and > with their entity equivalents. 
        3. Python: The html.escape() function (available since Python 3.2) handles standard escaping, while cgi.escape() 
        (older versions) primarily targets &, <, and >. 
        4. Online Tools: Free utilities exist to instantly convert text into HTML entities for use in templates, email 
        content, or code samples. 
        """
        # To Unescape from the HTML entities (Using python html module)
        q_text = unescape(self.current_question.text)

        return f"Q.{self.question_number}: {q_text}"

        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False