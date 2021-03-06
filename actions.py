# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_database_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        area_of_study_student = tracker.get_slot('area_of_study')
        var = area_of_study_student + "Hi"
        # print(area_of_study_student)

        if area_of_study_student in ("nursing"):
            utter_database_link = "In that case, I recommend searching CINAHL database at https://libguides.uta.edu/cinahl \
                                    If you are off-campus, you will be prompted to log in using your NetID username\
                                    and password. Also, you can open this link: https://libguides.uta.edu/NursingInfo. Once you open the link, \
                                    click on the Databases tab, and you may select one of the database  with the Best Bets. Additional database \
                                    are also listed here."
        elif area_of_study_student == "social_work":
            utter_database_link = "In that case, I recommend opening this link: https://libguides.uta.edu/SocialWorkInfo. Once you open the link, \
            click on the Databases tab, and you may select one of the database  with the Best Bets. Additional database \
            are also listed here."
        elif area_of_study_student == "business":
            utter_database_link = "In that case, I recommend opening this link: https://libguides.uta.edu/BusinessInfo. Once you open the link, \
            click on the Databases tab, and you may select one of the database  with the Best Bets. Additional database \
            are also listed here."
        elif area_of_study_student == "history":
            utter_database_link = "In that case, I recommend opening this link: https://libguides.uta.edu/HistoryInfo. Once you open the link, \
            click on the Databases tab, and you may select one of the database  with the Best Bets. Additional database \
            are also listed here."
        elif area_of_study_student == "history":
            utter_database_link = "In that case, I recommend opening this link: https://libguides.uta.edu/EnglishInfo. Once you open the link, \
            click on the Databases tab, and you may select one of the database  with the Best Bets. Additional database \
            are also listed here."
        elif area_of_study_student == "chemistry":
            utter_database_link = "In that case, I recommend opening this link: https://libguides.uta.edu/CHEMInfo. Once you open the link, \
            click on the Databases tab, and you may select one of the database  with the Best Bets. Additional database \
            are also listed here."
        else:
            utter_database_link = "In that case, I recommend opening the link: https://libguides.uta.edu/sb.php. \
            Please select a subject from the dropdown, and you will be guided to the homepage of the subject. Click on the database tab, and \
            you may select one of the database  with the Best Bets. Additional database are also listed here." 
        dispatcher.utter_message(utter_database_link)

        return []
