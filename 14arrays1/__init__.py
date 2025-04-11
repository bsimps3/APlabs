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
        
#

@check50.check()
def sumlastrunner_compiles():
    check50_java.compile("SumLastRunner.java")
    
@check50.check(sumlastrunner_compiles)
def sumlastrunner_main_exists():
    """SumLastRunner can run"""
    check50_java.checks.is_application_class("SumLastRunner")
    
@check50.check(sumlastrunner_main_exists)
def sumlastrunner_main_output():
    """SumLastRunner.main() output matches expected """
    expected = "40\n55\n230\n-1\n-1\n119\n-1\n45\n24\n-1\n356\n10011\n"
    actual = check50_java.run("SumLastRunner").stdout()
    help_msg = "Drats! Your output did not match expected. Make sure your input data is an exact match OR your code is working"
    if actual != expected:
        raise check50.Mismatch(expected, actual, help=help_msg)