import csv
from fpdf import FPDF

# Read data from CSV
def read_data(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({
                'Name': row['Name'],
                'Score': int(row['Score']),
                'Age': int(row['Age'])
            })
    return data

# Analyze data: calculate average score and age
def analyze_data(data):
    total_score = sum(item['Score'] for item in data)
    total_age = sum(item['Age'] for item in data)
    count = len(data)
    avg_score = total_score / count if count else 0
    avg_age = total_age / count if count else 0
    return avg_score, avg_age

# Generate PDF report
def generate_pdf_report(data, avg_score, avg_age, output_file='report.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)

    pdf.cell(0, 10, "Automated Data Analysis Report", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Total Records: {len(data)}", ln=True)
    pdf.cell(0, 10, f"Average Score: {avg_score:.2f}", ln=True)
    pdf.cell(0, 10, f"Average Age: {avg_age:.2f}", ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Detailed Data:", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", size=12)
    # Table headers
    pdf.cell(60, 10, "Name", 1)
    pdf.cell(40, 10, "Score", 1)
    pdf.cell(40, 10, "Age", 1)
    pdf.ln()

    # Table rows
    for item in data:
        pdf.cell(60, 10, item['Name'], 1)
        pdf.cell(40, 10, str(item['Score']), 1)
        pdf.cell(40, 10, str(item['Age']), 1)
        pdf.ln()

    pdf.output(output_file)
    print(f"Report generated and saved as '{output_file}'")

def main():
    data_file = 'data.csv'
    data = read_data(data_file)
    avg_score, avg_age = analyze_data(data)
    generate_pdf_report(data, avg_score, avg_age)

if __name__ == "__main__":
    main()
