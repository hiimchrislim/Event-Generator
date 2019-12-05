from flask import Flask, render_template, redirect, url_for, jsonify
from Calendar import WebScraper, Calendar

app = Flask(__name__, template_folder='templates')

ws = WebScraper()
ws.start_scrape()


@app.route('/events/<month>', methods=['GET'])
def monthly_events(month):
    """Subroute"""
    calendar = Calendar(ws.get_important_dates())
    # return render_template('home.html', important_dates=calendar.get_month_event(month))
    return jsonify(calendar.get_month_event(month))

@app.route('/', methods=['GET'])
@app.route('/events/', methods=['GET'])
def events():
    """Main Route"""
    calendar = Calendar(ws.get_important_dates())
    # return render_template('home.html', important_dates=calendar.get_all_events())
    return jsonify(calendar.get_all_events())

@app.errorhandler(404)
@app.errorhandler(500)
@app.errorhandler(502)
def page_not_found(e):
    """Redirect on all non-route events"""
    print(e)  # 404 and 500
    return redirect(url_for('events'))


if __name__ == '__main__':
    app.run()

"""
    <!--{% for month in important_dates %}-->
        <!--{% for important_date_obj in month %}-->
            <!--{{important_date}}-->
            <!--hi-->
        <!--{% endfor %}-->
    <!--{% endfor %}-->
"""
