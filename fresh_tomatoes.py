import webbrowser
import os


# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Run Wear Suggester</title>
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="css/main.css">
</head>

  <body>
      <div class="container">
        <div class="row text-center">
            <div class="col-md-12">
                <h1>Clothing Suggestions</h1>
            </div>
        </div>

        <div class="row text-center">
            <div class="col-md-4">
                <h2>Today</h2>
                <img class="clothing-img" src="images/tshirt.png">
                <img class="clothing-img" src="images/shorts.png">
            </div>  
            <div class="col-md-4">
                <h2>Tomorrow</h2>
                <img class="clothing-img" src="images/tshirt.png">
                <img class="clothing-img" src="images/shorts.png">
            </div>  
            <div class="col-md-4">
                <h2>Tomorrow + 1</h2>
                <img class="clothing-img" src="images/tshirt.png">
                <img class="clothing-img" src="images/shorts.png">
            </div>  
      </div>
  </body>
</html>
'''



def write_html():
    output_file = open('clothing.html', 'w')
    output_file.write(main_page_content)
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)


write_html()
