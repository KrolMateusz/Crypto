from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class StudentsListButton(ListItemButton):
    pass


class StudentDB(BoxLayout):
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    students_list = ObjectProperty()

    def submit_student(self):
        # Get the students name from TextInput
        student_name = self.first_name_text_input.text + ' ' + \
                       self.last_name_text_input.text
        # Add to ListView
        self.students_list.adapter.data.extend([student_name])
        # Reset the ListView
        self.students_list._trigger_reset_populate()

    def delete_student(self):
        # If a ListItem is selected
        if self.students_list.adapter.selection:
            # Get the text from selected
            selection = self.students_list.adapter.selection[0].text
            # Remove the matching item
            self.students_list.adapter.data.remove(selection)
            # Reset the ListView
            self.students_list._trigger_reset_populate()

    def replace_student(self):
        # If a ListItem is selected
        if self.students_list.adapter.selection:
            # Get the text from selected
            selection = self.students_list.adapter.selection[0].text
            # Remove the matching item
            self.students_list.adapter.data.remove(selection)
            # Get the students name from TextInput
            student_name = self.first_name_text_input.text + ' ' + \
                           self.last_name_text_input.text
            # Add the updated data to the list
            self.students_list.adapter.data.extend([student_name])
            # Reset the ListView
            self.students_list._trigger_reset_populate()


class StudentDBApp(App):
    def build(self):
        return StudentDB()


if __name__ == '__main__':
    StudentDBApp().run()
