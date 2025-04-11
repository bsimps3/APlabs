import check50
import check50_java

@check50.check()
def totalrunner_compiles():
    check50_java.compile("TotalRunner.java")
    
@check50.check(totalrunner_compiles)
def totalrunner_main_exists():
    """TotalRunner is application class"""
    check50_java.checks.is_application_class("TotalRunner")
    
@check50.check(totalrunner_main_exists)
def totalrunner_main_output():
    """TotalRunner.main() output matches """
    expected = "12301\n-44\n-11568\n32767\n510\n476\n497\n-35\n-947\n1089\n-99\n6011\n"
    actual = check50_java.run("TotalRunner").stdout()
    help_msg = "your output did not match expected. Make sure your input data is an exact match"
    if actual != expected:
        raise check50.Mismatch(expected, actual, help=help_msg)