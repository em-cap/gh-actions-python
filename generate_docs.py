"""
Generate test results for documentation.
This script runs after tests to create a summary for the website.
"""

import json
import subprocess
import sys
from datetime import datetime


def run_tests():
    """Run tests and capture basic results."""
    try:
        result = subprocess.run(
            ["python", "-m", "pytest", "test_calculator.py", "-v"], 
            capture_output=True, 
            text=True
        )
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), 1


def generate_test_report():
    """Generate a simple test report."""
    stdout, stderr, returncode = run_tests()
    
    # Count test results from output
    passed = stdout.count(" PASSED")
    failed = stdout.count(" FAILED")
    total = passed + failed
    
    test_data = {
        "timestamp": datetime.now().isoformat(),
        "success": returncode == 0,
        "summary": {
            "total": total,
            "passed": passed,
            "failed": failed
        }
    }
    
    # Save results
    with open('docs/test-results.json', 'w') as f:
        json.dump(test_data, f, indent=2)
    
    return test_data


def update_html_with_results(test_data):
    """Update the HTML file with test results."""
    try:
        with open('docs/index.html', 'r') as f:
            content = f.read()
        
        # Create test results section
        test_summary = f"""
        <div style="background: #d4edda; border: 1px solid #c3e6cb; border-radius: 4px; padding: 15px; margin: 15px 0;">
            <h4 style="margin: 0 0 10px 0; color: #155724;">Latest Test Results</h4>
            <p style="margin: 5px 0;"><strong>Total Tests:</strong> {test_data['summary']['total']}</p>
            <p style="margin: 5px 0;"><strong>Passed:</strong> <span style="color: #28a745;">{test_data['summary']['passed']}</span></p>
            <p style="margin: 5px 0;"><strong>Failed:</strong> <span style="color: #dc3545;">{test_data['summary']['failed']}</span></p>
            <p style="margin: 5px 0;"><strong>Status:</strong> {'✅ All tests passing' if test_data['success'] else '❌ Some tests failing'}</p>
            <p style="margin: 5px 0; font-size: 0.9em; color: #666;"><strong>Last Run:</strong> {test_data['timestamp'][:19]}</p>
        </div>
        """
        
        # Insert after the "Test Results" heading
        content = content.replace(
            '<h2>📈 Test Results</h2>\n        <p>Latest build results and coverage reports are automatically generated and can be viewed in the GitHub Actions tab.</p>',
            f'<h2>📈 Test Results</h2>{test_summary}'
        )
        
        with open('docs/index.html', 'w') as f:
            f.write(content)
            
        print("✅ Updated HTML with test results")
        
    except Exception as e:
        print(f"⚠️  Could not update HTML: {e}")


if __name__ == "__main__":
    print("🧪 Generating test report...")
    test_data = generate_test_report()
    
    print(f"📊 Test Summary:")
    print(f"   Total: {test_data['summary']['total']}")
    print(f"   Passed: {test_data['summary']['passed']}")
    print(f"   Failed: {test_data['summary']['failed']}")
    print(f"   Status: {'PASS' if test_data['success'] else 'FAIL'}")
    
    update_html_with_results(test_data)
    
    # Exit with appropriate code
    sys.exit(0 if test_data['success'] else 1)