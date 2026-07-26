class QualityEngine:


    def __init__(self):

        self.minimum_score = 90



    def analyze(
            self,
            test_result,
            review_result
    ):


        score = 100


        if "FAILED" in str(test_result):

            score -= 40


        if "NEEDS_FIX" in str(review_result):

            score -= 30


        if "error" in str(test_result).lower():

            score -= 20



        if score < 0:

            score = 0



        return {

            "score": score,

            "passed":
                score >= self.minimum_score,

            "quality":
                self.get_quality(score)

        }




    def get_quality(
            self,
            score
    ):


        if score >= 90:

            return "excellent"


        if score >= 70:

            return "good"


        if score >= 40:

            return "weak"


        return "bad"
