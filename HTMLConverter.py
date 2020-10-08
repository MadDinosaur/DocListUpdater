from bs4 import BeautifulSoup

# HTML FILE PATH
html_file_path = "index.html"
# LIBRARY USAGE
file = open(html_file_path, 'r')
html = BeautifulSoup(file, 'html.parser')
file.close()
# HTML RESOURCES
copy_button_src = 'M320 448v40c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V120c0-13.255 10.745-24 24-24h72v296c0 30.879 25.121 56 56 56h168zm0-344V0H152c-13.255 0-24 10.745-24 24v368c0 13.255 10.745 24 24 24h272c13.255 0 24-10.745 24-24V128H344c-13.2 0-24-10.8-24-24zm120.971-31.029L375.029 7.029A24 24 0 0 0 358.059 0H352v96h96v-6.059a24 24 0 0 0-7.029-16.97z'
download_button_src = 'M224 136V0H24C10.7 0 0 10.7 0 24v464c0 13.3 10.7 24 24 24h336c13.3 0 24-10.7 24-24V160H248c-13.2 0-24-10.8-24-24zm76.45 211.36l-96.42 95.7c-6.65 6.61-17.39 6.61-24.04 0l-96.42-95.7C73.42 337.29 80.54 320 94.82 320H160v-80c0-8.84 7.16-16 16-16h32c8.84 0 16 7.16 16 16v80h65.18c14.28 0 21.4 17.29 11.27 27.36zM377 105L279.1 7c-4.5-4.5-10.6-7-17-7H256v128h128v-6.1c0-6.3-2.5-12.4-7-16.9z'

copy_button_img = html.new_tag('svg', None, None, {'viewBox': '0 0 448 512', 'width': '20'})
copy_button_img.append(html.new_tag('path', None, None, {'d': copy_button_src}))

download_button_img = html.new_tag('svg', None, None, {'viewBox': '0 0 448 512', 'width': '20'})
download_button_img.append(html.new_tag('path', None, None, {'d': download_button_src}))


def add_line(file_list_type, file_list_filename, file_list_location, file_list_path):
    new_entry = html.new_tag('tr')
    # TYPE COLUMN
    col_one = html.new_tag('td', None, None, {'height': 19})
    col_one.string = file_list_type
    new_entry.contents.append(col_one)
    ##
    # DESCRIPTION COLUMN
    col_two = html.new_tag('td')
    col_two.string = file_list_filename
    new_entry.contents.append(col_two)
    ##
    # FILENAME COLUMN
    col_three = html.new_tag('td')
    italic = html.new_tag('i')
    italic.string = file_list_filename
    col_three.append(italic)
    new_entry.contents.append(col_three)
    ##
    # DOWNLOAD/COPY BUTTONS COLUMN
    col_four = html.new_tag('td')
    tooltip_div = html.new_tag('div', None, None, {'class': 'tooltip'})

    copy = html.new_tag('button', None, None,
                        {'src': file_list_location, 'title': 'Copy to clipboard', 'onclick': 'copyToClipboard(this)'})
    copy.append(copy_button_img)

    download = html.new_tag('a', None, None, {'href': file_list_path, 'title': 'Download', 'target': '_blank'})
    download_button = html.new_tag('button')
    download.append(download_button)
    download_button.append(download_button_img)

    tooltip_div.append(copy)
    tooltip_div.append(download)
    col_four.append(tooltip_div)
    new_entry.contents.append(col_four)
    ##

    last_tag = html.find_all('td')[-1]
    last_tag.insert_after(new_entry)


def writeToHTML():
    file = open(html_file_path, 'w')

    html.encode('utf-8')
    file.write(html.prettify(formatter= 'html'))

    file.close()
