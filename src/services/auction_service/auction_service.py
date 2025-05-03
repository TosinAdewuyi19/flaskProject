
class AuctionService:
    def __init__(self):
        self.auctions = []

    def create_auction(self, auction_data):
        auction_id = len(self.auctions) + 1
        auction = {
            "id": auction_id,
            "name": auction_data.get("name"),
            "description": auction_data.get("description"),
            "seller": auction_data.get("seller")
        }
        self.auctions.append(auction)
        print("Auction created:", auction)
        return auction

    def get_auctions_by_seller(self, seller):
        seller_auctions = [auction for auction in self.auctions if auction['seller'] == seller]
        return seller_auctions

    def get_all_auctions(self):
        return self.auctions

    def delete_auction(self, auction_id):
        for auction in self.auctions:
            if auction['id'] == auction_id:
                self.auctions.remove(auction)
                print("Auction deleted:", auction)
                return auction
        raise ValueError("Auction not found.")

auction_service = AuctionService()