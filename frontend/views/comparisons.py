import streamlit as st


def render_comparison_view():
    st.markdown(
        """
<main class="page-pad">
    <h1 class="page-title">Model Comparison</h1>
    <p class="page-subtitle">Compare different response generation approaches.</p>
    <section class="comparison-card">
        <table class="comparison-table">
            <thead>
                <tr>
                    <th>Query / Scenario</th>
                    <th>Baseline<br><span style="font-weight:600;font-size:12px;color:#5d6b7e">(Zero-shot)</span></th>
                    <th>Rule-Based</th>
                    <th>Retrieval-Based</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Order delayed</td>
                    <td>We apologize for the inconvenience.</td>
                    <td>Our order delay policy allows 3-5 business days.</td>
                    <td>Your order is delayed due to high demand. It will reach you soon.</td>
                </tr>
                <tr>
                    <td>Need refund</td>
                    <td>Please contact our support team.</td>
                    <td>Refunds are processed within 5-7 business days.</td>
                    <td>We have initiated your refund. It will reflect in your account within 5 business days.</td>
                </tr>
                <tr>
                    <td>Damaged product</td>
                    <td>We are sorry about the issue.</td>
                    <td>Damaged items are eligible for replacement within 7 days.</td>
                    <td>We understand the issue. A replacement has been initiated.</td>
                </tr>
            </tbody>
        </table>
        <div class="table-note">* Retrieval-Based model shows highest contextual relevance.</div>
    </section>
</main>
<style>
    .comparison-card {
        border: 1px solid #e8edf4;
        border-radius: 8px;
        box-shadow: 0 4px 18px rgba(16,33,60,.07);
        overflow: hidden;
        background: #fff;
    }
    .comparison-table {
        width: 100%;
        border-collapse: collapse;
        color: #26344a;
    }
    .comparison-table th {
        background: #f8fafc;
        color: #2d3b50;
        font-size: 14px;
        font-weight: 800;
        line-height: 1.35;
        text-align: left;
        padding: 24px 28px;
        border-bottom: 1px solid #edf1f6;
    }
    .comparison-table td {
        width: 25%;
        padding: 28px;
        border-bottom: 1px solid #edf1f6;
        border-right: 1px solid #edf1f6;
        vertical-align: top;
        color: #2f3b4e;
        font-size: 15px;
        font-weight: 600;
        line-height: 1.6;
    }
    .comparison-table td:first-child {
        color: #2c3748;
        font-weight: 800;
    }
    .comparison-table td:last-child {
        border-right: 0;
    }
    .comparison-table tr:last-child td {
        border-bottom: 0;
    }
    .table-note {
        border-top: 1px solid #edf1f6;
        padding: 16px 28px;
        color: #405168;
        font-size: 13px;
        font-weight: 700;
    }
</style>
""",
        unsafe_allow_html=True,
    )
