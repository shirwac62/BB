"""
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        bgroup = request.form["bgroup"]
        bpackets = request.form["bpackets"]
        fname = request.form["fname"]
        adress = request.form["adress"]

        # create a cursor
        # cur = mysql.connection.cursor()

        # Inserting values into tables
        # cur.execute("INSERT INTO CONTACT(B_GROUP,C_PACKETS,F_NAME,ADRESS) VALUES(%s, %s, %s, %s)",
        #             (bgroup, bpackets, fname, adress))
        # cur.execute("INSERT INTO NOTIFICATIONS(NB_GROUP,N_PACKETS,NF_NAME,NADRESS) VALUES(%s, %s, %s, %s)",
        #             (bgroup, bpackets, fname, adress))
        # Commit to DB
        # mysql.connection.commit()
        # close connection
        # cur.close()
        flash('Your request is successfully sent to the Blood Bank', 'success')
        return redirect(url_for('index'))

    return render_template('contact.html')












@app.route('/donate', methods=['GET', 'POST'])
@is_logged_in
def donate():
    if request.method == 'POST':
        # Get Form Fields
        dname = request.form["dname"]
        sex = request.form["sex"]
        age = request.form["age"]
        weight = request.form["weight"]
        address = request.form["address"]
        disease = request.form["disease"]
        demail = request.form["demail"]

        # create a cursor
        # cur = mysql.connection.cursor()
        #
        # # Inserting values into tables
        # cur.execute("INSERT INTO DONOR(DNAME,SEX,AGE,WEIGHT,ADDRESS,DISEASE,DEMAIL) VALUES(%s, %s, %s, %s, %s, %s, %s)",
        #             (dname, sex, age, weight, address, disease, demail))
        # # Commit to DB
        # mysql.connection.commit()
        # # close connection
        # cur.close()
        flash('Success! Donor details Added.', 'success')
        return redirect(url_for('donorlogs'))

    return render_template('donate.html')


@app.route('/donorlogs')
@is_logged_in
def donorlogs():



@app.route('/bloodform', methods=['GET', 'POST'])
@is_logged_in
def bloodform():
    if request.method == 'POST':
        # Get Form Fields
        d_id = request.form["d_id"]
        blood_group = request.form["blood_group"]
        packets = request.form["packets"]

        # create a cursor
        # cur = mysql.connection.cursor()
        #
        # # Inserting values into tables
        # cur.execute("INSERT INTO BLOOD(D_ID,B_GROUP,PACKETS) VALUES(%s, %s, %s)", (d_id, blood_group, packets))
        # cur.execute("SELECT * FROM BLOODBANK")
        # records = cur.fetchall()
        # cur.execute("UPDATE BLOODBANK SET TOTAL_PACKETS = TOTAL_PACKETS+%s WHERE B_GROUP = %s", (packets, blood_group))
        # # Commit to DB
        # mysql.connection.commit()
        # # close connection
        # cur.close()
        flash('Success! Donor Blood details Added.', 'success')
        return redirect(url_for('dashboard'))

    return render_template('add_blood.html')


@app.route('/notifications')
@is_logged_in
def notifications():
    # cur = mysql.connection.cursor()
    # result = cur.execute("SELECT * FROM CONTACT")
    # requests = cur.fetchall()
    #
    # if result > 0:
    #     return render_template('notification.html', requests=requests)
    # else:
    #     msg = ' No requests found '
    #     return render_template('notification.html', msg=msg)
    # # close connection
    # cur.close()
    return None


@app.route('/notifications/accept')
@is_logged_in
def accept():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT N_PACKETS FROM NOTIFICATIONS")
    # packets = cur.fetchone()
    # packet = (x[0] for x in packets)
    # cur.execute("SELECT NB_GROUP FROM NOTIFICATIONS")
    # groups = cur.fetchone()
    # group = (y[0] for y in groups)
    #
    # # for row in allnotifications:
    # #      group = row[1]
    # #      packet = row[2]
    # cur.execute("UPDATE BLOODBANK SET TOTAL_PACKETS = TOTAL_PACKETS-%s WHERE B_GROUP = %s",(packet[-1],group[-1]))
    # result = "ACCEPTED"
    # cur.execute("INSERT INTO NOTIFICATIONS(RESULT) VALUES(%s)",(result))
    flash('Request Accepted', 'success')
    return redirect(url_for('notifications'))


@app.route('/notifications/decline')
@is_logged_in
def decline():
    msg = 'Request Declined'
    flash(msg, 'danger')
    return redirect(url_for('notifications'))







"""""
